from . import BaseModel
from contextlib import suppress
import re
from pydantic import Field
from typing import Any, List, Union
from . import nikola
from enum import Enum
from ..paths import Path
import datetime

FRONT_MATTER = re.compile(r"^[-\s*]{3,}\n", re.MULTILINE)


class Document(BaseModel):
    path: Any
    source: Any = None
    metadata: dict = Field(default_factory=dict)
    has_front_matter: bool = False
    body: Union[dict, str] = ""

    def load(self):
        self.source = Path(self.path).load()
        if isinstance(self.source, str):
            data, *rest = FRONT_MATTER.split(self.source, 2)
            self.has_front_matter = (len(rest) == 2) and not bool(data.strip())

            if self.has_front_matter:
                import yaml

                self.metadata, self.body = rest
                self.metadata = yaml.safe_load(self.metadata)

        elif self.path in {".ipynb"}:
            self.metadata.update(self.source["metadata"])

        return self

    def to_new_source(self, write=False):
        if isinstance(self.source, str):
            import yaml

            return (
                r"---\n" + yaml.safe_dump(self.metadata or {}) + r"\n---\n" + self.body
            )
        else:
            source = self.source.copy()
            source["metadata"].uppdate(self.metadata)

            return source


class Notebook(Document):
    format = ".ipynb"
    # should do smart things with jupytext here


class Markdown(Notebook):
    format = ".md"


class Rst(Notebook):
    format = ".rst"


class Page(BaseModel):
    """a model for page specific configuration data"""

    path: Any
    title: str = None
    date: Any = Field(default_factory=datetime.date.today)
    name: str = None
    email: str = None
    description: str = ""
    url: str = "https://"
    has_excerpt: bool = False
    is_sphinx: bool = False
    is_nikola: bool = False
    is_missing: List = Field(default_factory=list)
    document: Any = None

    tags: List = Field(default_factory=list)
    category: str = None

    def to_nikola_front_matter(self):
        return nikola.Metadata(
            title=self.title,
            date=self.date,
            description=self.description,
            tags=self.tags,
            category=self.category,
        )

    def __post_init__(self):
        self.document = Document(path=self.path)

    def load(self):
        self.document.load()
        return self
