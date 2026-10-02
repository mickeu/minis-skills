#!/usr/bin/env python3
"""tg-hub: configuration from environment variables."""

import os
from pathlib import Path

# --- Defaults ---
_DEFAULT_API_ID = 2040
_DEFAULT_API_HASH = "b18441a1ff542e47e2b6a8f0a4d1d8d3"
_DEFAULT_DATA_DIR = os.path.expanduser("~/.tg-hub")


class Config:
    """Read config from environment variables with sensible defaults."""

    def __init__(self):
        self.api_id = int(os.getenv("TG_API_ID", _DEFAULT_API_ID))
        self.api_hash = os.getenv("TG_API_HASH", _DEFAULT_API_HASH)

        data_dir = os.getenv("TG_DATA_DIR", _DEFAULT_DATA_DIR)
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.session_name = os.getenv("TG_SESSION_NAME", "tg_hub")
        self.session_path = self.data_dir / f"{self.session_name}.session"

        self.db_path = os.getenv("TG_DB_PATH", str(self.data_dir / "messages.db"))

        self.device_model = os.getenv("TG_DEVICE_MODEL", "Desktop")
        self.system_version = os.getenv("TG_SYSTEM_VERSION", "macOS 15.3")
        self.app_version = os.getenv("TG_APP_VERSION", "5.12.1")
        self.lang_code = os.getenv("TG_LANG_CODE", "en")
        self.system_lang_code = os.getenv("TG_SYSTEM_LANG_CODE", "en-US")

        self._warn_default = (
            self.api_id == _DEFAULT_API_ID and self.api_hash == _DEFAULT_API_HASH
        )

    @property
    def using_default_credentials(self) -> bool:
        return self._warn_default


config = Config()