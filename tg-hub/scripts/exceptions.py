#!/usr/bin/env python3
"""tg-hub: structured exceptions."""


class TGHubError(Exception):
    """Base exception for tg-hub."""


class LoginError(TGHubError):
    """Login failed."""


class SyncError(TGHubError):
    """Message sync failed."""


class ConfigError(TGHubError):
    """Configuration error."""


class DatabaseError(TGHubError):
    """Database operation failed."""