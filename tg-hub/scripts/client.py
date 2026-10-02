#!/usr/bin/env python3
"""tg-hub: TGClient — Telethon wrapper with local SQLite storage."""

import json
import time
import logging
from typing import Optional

from telethon import TelegramClient, sync  # noqa: F401 — needed for sync behavior
from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import Message, Channel, Chat, User

from scripts.config import config
from scripts.db import DB
from scripts.exceptions import LoginError, SyncError

logger = logging.getLogger("tg-hub")


class TGClient:
    """Core Telegram client with local-first message storage."""

    def __init__(self, db: Optional[DB] = None):
        self._db = db or DB()
        self._client: Optional[TelegramClient] = None
        self._me: Optional[dict] = None

    def _get_client(self) -> TelegramClient:
        if self._client is None:
            if config.using_default_credentials:
                logger.warning(
                    "Using default api_id=2040 / built-in api_hash. "
                    "Set TG_API_ID / TG_API_HASH env vars for your own credentials."
                )
            self._client = TelegramClient(
                str(config.session_path),
                config.api_id,
                config.api_hash,
                device_model=config.device_model,
                system_version=config.system_version,
                app_version=config.app_version,
                lang_code=config.lang_code,
                system_lang_code=config.system_lang_code,
            )
            self._client.start()
            self._me = self._client.get_me()
        return self._client

    def login(self) -> dict:
        """Interactive login — prints phone/verification prompts."""
        client = TelegramClient(
            str(config.session_path),
            config.api_id,
            config.api_hash,
            device_model=config.device_model,
            system_version=config.system_version,
            app_version=config.app_version,
            lang_code=config.lang_code,
            system_lang_code=config.system_lang_code,
        )
        try:
            client.start()
        except SessionPasswordNeededError:
            pwd = input("Two-factor authentication password: ")
            client.sign_in(password=pwd)

        me = client.get_me()
        self._client = client
        self._me = me
        result = {
            "id": me.id,
            "name": me.first_name or "",
            "phone": me.phone or "",
            "username": me.username or "",
        }
        print(f"\n✅ 登录成功: {result['name']} ({result['phone'] or result['username']})")
        return result

    def whoami(self) -> dict:
        c = self._get_client()
        me = c.get_me()
        return {
            "id": me.id,
            "name": me.first_name or "",
            "phone": me.phone or "",
            "username": me.username or "",
        }

    def list_chats(self, chat_type: Optional[str] = None) -> list[dict]:
        """List all dialogs from Telegram (live)."""
        c = self._get_client()
        results = []
        for dialog in c.get_dialogs():
            entity = dialog.entity
            if chat_type and chat_type not in str(type(entity).__name__).lower():
                continue
            t = "channel" if isinstance(entity, Channel) else (
                "group" if isinstance(entity, Chat) else (
                    "bot" if getattr(entity, "bot", False) else "user"
                )
            )
            results.append({
                "id": entity.id,
                "name": dialog.name or "Unknown",
                "type": t,
                "unread": dialog.unread_count,
                "top_message_id": dialog.top_message.id if dialog.top_message else None,
            })
        return results

    def sync(self, chat: str, limit: int = 5000) -> int:
        """Sync a single chat/group/channel to local SQLite. Returns new message count."""
        c = self._get_client()
        entity = c.get_entity(chat)
        chat_name = getattr(entity, "title", None) or getattr(entity, "username", None) or chat
        chat_id = entity.id

        # Get the latest message ID we have locally
        last_id = self._db._conn.execute(
            "SELECT COALESCE(MAX(id), 0) FROM messages WHERE chat_id = ?", [chat_id]
        ).fetchone()[0]

        # Cap limit for first sync
        if last_id == 0 and limit > 2000:
            limit = 2000

        offset_id = last_id if last_id > 0 else 0
        new_count = 0

        try:
            for msg in c.iter_messages(entity, limit=limit, offset_id=offset_id, reverse=True):
                if not isinstance(msg, Message):
                    continue
                content = msg.text or msg.message or ""
                if not content and msg.media:
                    content = f"[media: {type(msg.media).__name__}]"

                sender_name = ""
                sender_id = None
                if msg.sender_id:
                    sender_id = msg.sender_id
                    try:
                        sender = msg.get_sender()
                        if sender:
                            sender_name = (
                                getattr(sender, "first_name", "") or ""
                            )
                            if getattr(sender, "last_name", None):
                                sender_name += f" {sender.last_name}"
                            if not sender_name:
                                sender_name = getattr(sender, "username", "") or ""
                    except Exception:
                        sender_name = str(sender_id)

                raw_data = json.dumps({
                    k: v for k, v in msg.to_dict().items()
                    if k in ("id", "date", "peer_id", "from_id", "message", "media", "reply_to")
                }, default=str)

                added = self._db.upsert_message(
                    msg_id=msg.id,
                    chat_id=chat_id,
                    chat_name=chat_name,
                    sender_id=sender_id,
                    sender_name=sender_name,
                    content=content,
                    date=int(msg.date.timestamp()),
                    raw_data=raw_data,
                )
                if added:
                    new_count += 1
        except Exception as e:
            raise SyncError(f"Sync failed for {chat}: {e}") from e

        return new_count

    def sync_all(self, limit_per_chat: int = 5000, delay: float = 1.0, max_chats: Optional[int] = None) -> dict[str, int]:
        """Sync all dialogs."""
        c = self._get_client()
        results = {}
        for i, dialog in enumerate(c.get_dialogs()):
            if max_chats is not None and i >= max_chats:
                break
            name = dialog.name or "Unknown"
            try:
                count = self.sync(name, limit=limit_per_chat)
                results[name] = count
                if delay > 0 and count > 0:
                    time.sleep(delay)
            except Exception as e:
                logger.warning(f"Sync failed for {name}: {e}")
                results[name] = -1
        return results

    def refresh(self, limit_per_chat: int = 500, delay: float = 1.0, max_chats: Optional[int] = None) -> dict[str, int]:
        """Quick incremental refresh of all chats."""
        return self.sync_all(limit_per_chat=limit_per_chat, delay=delay, max_chats=max_chats)

    # --- Local queries (no network) ---

    def search(self, keyword: str, *, chat: Optional[str] = None, hours: Optional[int] = None,
               regex: bool = False, limit: int = 100) -> list[dict]:
        return self._db.search(keyword, chat=chat, hours=hours, regex=regex, limit=limit)

    def filter(self, keywords: str, *, chat: Optional[str] = None, hours: Optional[int] = None,
               limit: int = 100) -> list[dict]:
        return self._db.filter_keywords(keywords, chat=chat, hours=hours, limit=limit)

    def today(self, chat: Optional[str] = None) -> list[dict]:
        return self._db.today(chat=chat)

    def recent(self, hours: int = 24, *, chat: Optional[str] = None,
               sender: Optional[str] = None, limit: int = 100) -> list[dict]:
        return self._db.recent(hours=hours, chat=chat, sender=sender, limit=limit)

    def top_senders(self, chat: Optional[str] = None, hours: Optional[int] = None,
                    limit: int = 10) -> list[dict]:
        return self._db.top_senders(chat=chat, hours=hours, limit=limit)

    def timeline(self, chat: Optional[str] = None, hours: Optional[int] = None,
                 granularity: str = "hour") -> list[dict]:
        return self._db.timeline(chat=chat, hours=hours, granularity=granularity)

    def stats(self) -> dict:
        return self._db.stats()

    def local_chats(self) -> list[str]:
        return self._db.local_chats()

    def delete_chat(self, chat: str) -> int:
        return self._db.delete_chat(chat)