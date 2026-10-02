#!/usr/bin/env python3
"""tg-hub: SQLite message storage."""

import sqlite3
import time
from pathlib import Path
from typing import Optional

from scripts.config import config
from scripts.exceptions import DatabaseError

_SCHEMA = """
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY,
    chat_id INTEGER NOT NULL,
    chat_name TEXT NOT NULL DEFAULT '',
    sender_id INTEGER DEFAULT NULL,
    sender_name TEXT DEFAULT '',
    content TEXT DEFAULT '',
    date INTEGER NOT NULL,
    raw_data TEXT DEFAULT ''
);

CREATE INDEX IF NOT EXISTS idx_messages_chat ON messages(chat_id);
CREATE INDEX IF NOT EXISTS idx_messages_date ON messages(date);
CREATE INDEX IF NOT EXISTS idx_messages_chat_date ON messages(chat_id, date);
"""


class DB:
    """SQLite wrapper for message storage."""

    def __init__(self, db_path: Optional[str] = None):
        self._path = db_path or config.db_path
        Path(self._path).parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(self._path, check_same_thread=False)
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute("PRAGMA synchronous=NORMAL")
        self._init()

    def _init(self):
        self._conn.executescript(_SCHEMA)
        self._conn.commit()

    def _row_to_dict(self, row) -> dict:
        cols = ["id", "chat_id", "chat_name", "sender_id", "sender_name", "content", "date", "raw_data"]
        return dict(zip(cols, row))

    def upsert_message(
        self, msg_id: int, chat_id: int, chat_name: str,
        sender_id: Optional[int], sender_name: str,
        content: str, date: int, raw_data: str = ""
    ) -> bool:
        """Insert or ignore (keep existing row on conflict)."""
        try:
            self._conn.execute(
                """INSERT OR IGNORE INTO messages
                   (id, chat_id, chat_name, sender_id, sender_name, content, date, raw_data)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (msg_id, chat_id, chat_name, sender_id, sender_name, content, date, raw_data),
            )
            self._conn.commit()
            return self._conn.total_changes > 0
        except sqlite3.Error as e:
            raise DatabaseError(f"Insert failed: {e}") from e

    def search(
        self, keyword: str, *, chat: Optional[str] = None,
        hours: Optional[int] = None, regex: bool = False, limit: int = 100
    ) -> list[dict]:
        """Search messages by keyword."""
        sql = "SELECT * FROM messages WHERE 1=1"
        params = []

        if chat:
            sql += " AND chat_name = ?"
            params.append(chat)
        if hours is not None:
            cutoff = int(time.time()) - hours * 3600
            sql += " AND date >= ?"
            params.append(cutoff)

        if regex:
            try:
                import re as re_mod
                # Use SQLite REGEXP via Python — load extension or fallback to Python filter
                rows = self._conn.execute(sql, params).fetchall()
                pat = re_mod.compile(keyword)
                result = [self._row_to_dict(r) for r in rows if pat.search(r[5] or "")]
                return result[:limit]
            except Exception:
                pass

        sql += " AND content LIKE ?"
        params.append(f"%{keyword}%")
        sql += " ORDER BY date DESC LIMIT ?"
        params.append(limit)

        rows = self._conn.execute(sql, params).fetchall()
        return [self._row_to_dict(r) for r in rows]

    def filter_keywords(
        self, keywords: str, *, chat: Optional[str] = None,
        hours: Optional[int] = None, limit: int = 100
    ) -> list[dict]:
        """OR filter — match any keyword."""
        parts = [k.strip() for k in keywords.replace("，", ",").split(",") if k.strip()]
        if not parts:
            return []

        sql = "SELECT * FROM messages WHERE ("
        clauses = []
        params = []
        for p in parts:
            clauses.append("content LIKE ?")
            params.append(f"%{p}%")
        sql += " OR ".join(clauses) + ")"
        if chat:
            sql += " AND chat_name = ?"
            params.append(chat)
        if hours is not None:
            cutoff = int(time.time()) - hours * 3600
            sql += " AND date >= ?"
            params.append(cutoff)
        sql += " ORDER BY date DESC LIMIT ?"
        params.append(limit)

        rows = self._conn.execute(sql, params).fetchall()
        return [self._row_to_dict(r) for r in rows]

    def today(self, chat: Optional[str] = None) -> list[dict]:
        """Get today's messages."""
        import datetime
        today_start = int(
            datetime.datetime.combine(
                datetime.date.today(), datetime.time.min
            ).timestamp()
        )
        sql = "SELECT * FROM messages WHERE date >= ?"
        params = [today_start]
        if chat:
            sql += " AND chat_name = ?"
            params.append(chat)
        sql += " ORDER BY date DESC"
        rows = self._conn.execute(sql, params).fetchall()
        return [self._row_to_dict(r) for r in rows]

    def recent(
        self, hours: int = 24, *, chat: Optional[str] = None,
        sender: Optional[str] = None, limit: int = 100
    ) -> list[dict]:
        """Get recent messages."""
        cutoff = int(time.time()) - hours * 3600
        sql = "SELECT * FROM messages WHERE date >= ?"
        params = [cutoff]
        if chat:
            sql += " AND chat_name = ?"
            params.append(chat)
        if sender:
            sql += " AND sender_name = ?"
            params.append(sender)
        sql += " ORDER BY date DESC LIMIT ?"
        params.append(limit)
        rows = self._conn.execute(sql, params).fetchall()
        return [self._row_to_dict(r) for r in rows]

    def top_senders(
        self, chat: Optional[str] = None, hours: Optional[int] = None, limit: int = 10
    ) -> list[dict]:
        """Rank top senders by message count."""
        sql = "SELECT sender_name, COUNT(*) as msg_count FROM messages WHERE sender_name != ''"
        params = []
        if chat:
            sql += " AND chat_name = ?"
            params.append(chat)
        if hours is not None:
            cutoff = int(time.time()) - hours * 3600
            sql += " AND date >= ?"
            params.append(cutoff)
        sql += " GROUP BY sender_name ORDER BY msg_count DESC LIMIT ?"
        params.append(limit)
        rows = self._conn.execute(sql, params).fetchall()
        return [{"sender_name": r[0], "msg_count": r[1]} for r in rows]

    def timeline(
        self, chat: Optional[str] = None, hours: Optional[int] = None,
        granularity: str = "hour"
    ) -> list[dict]:
        """Message count timeline."""
        import datetime
        cutoff = int(time.time()) - (hours or 48) * 3600 if hours else 0
        rows = self._conn.execute(
            "SELECT date, content FROM messages WHERE date >= ?", [cutoff]
        ).fetchall()

        buckets: dict[str, int] = {}
        for date, _ in rows:
            dt = datetime.datetime.fromtimestamp(date)
            if granularity == "hour":
                key = dt.strftime("%Y-%m-%d %H:00")
            elif granularity == "day":
                key = dt.strftime("%Y-%m-%d")
            elif granularity == "minute":
                key = dt.strftime("%Y-%m-%d %H:%M")
            else:
                key = dt.strftime("%Y-%m-%d %H:00")
            buckets[key] = buckets.get(key, 0) + 1

        return sorted(
            [{"time": k, "count": v} for k, v in buckets.items()],
            key=lambda x: x["time"],
        )

    def stats(self) -> dict:
        """Database statistics."""
        total = self._conn.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
        chats = [
            r[0] for r in self._conn.execute(
                "SELECT DISTINCT chat_name FROM messages WHERE chat_name != '' ORDER BY chat_name"
            ).fetchall()
        ]
        return {"total": total, "chats": chats}

    def local_chats(self) -> list[str]:
        return self.stats()["chats"]

    def delete_chat(self, chat: str) -> int:
        cur = self._conn.execute("DELETE FROM messages WHERE chat_name = ?", [chat])
        self._conn.commit()
        return cur.rowcount

    def close(self):
        self._conn.close()