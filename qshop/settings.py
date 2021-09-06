from enum import Enum
from pathlib import Path
from typing import Any, List

from pydantic import BaseSettings as _BaseSettings
from pydantic import Field

__all__ = "SETTINGS", "DOIT_CONFIG"


class BaseSettings(_BaseSettings):
    parent: _BaseSettings = None


class DoitBackend(Enum):
    json = "json"
    sqlite3 = "sqlite3"
    dbm = "dbm"


class Doit(BaseSettings):
    verbosity: int = 2
    backend: DoitBackend = "json"


class Settings(BaseSettings):
    doit: Doit = Field(default_factory=Doit)

    access_token: str = None
    cwd: Path = Field(default_factory=Path)
    output_dir: Path = "output"
    site: Any = None

    def set_site(self, site):
        from .models.site import Site

        if self.site is None:
            self.site = Site(id=site)

        return self.site


SETTINGS = Settings()
DOIT_CONFIG = dict(verbosity=2, backend="json")
