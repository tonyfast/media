from .models import BaseModel
from pydantic import BaseSettings, Field
from enum import Enum
from pathlib import Path
from typing import Any

__all__ = "SETTINGS", "DOIT_CONFIG"


class DoitBackend(Enum):
    json = "json"
    sqlite3 = "sqlite3"
    dbm = "dbm"


class Doit(BaseModel):
    verbosity: int = 2
    backend: DoitBackend = "json"


class Settings(BaseSettings):
    doit: Doit = Field(default_factory=Doit)
    access_token: str = None
    cwd: Path = Field(default_factory=Path)
    output_dir: Path = "output"
    toc: Path = Path("toc.yml")
    conf: Path = Path("conf.py")
    site_config: Path = Path("config.yml")
    site: Any = None

    def set_site(self, site):
        from .models.site import Site

        if self.site is None:
            self.site = Site(project=site)

        return self.site


SETTINGS = Settings()
DOIT_CONFIG = SETTINGS.doit.dict()
