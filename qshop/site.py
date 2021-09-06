"""Site is the top level class for managing our site"""


from enum import Enum
from pathlib import Path
from typing import List

from pydantic import Field

from . import OpenModel
from . import blog as _blog
from . import git as _git
from . import github as _github
from . import sphinx as _sphinx


class Format(Enum):
    """formats for content, use for glob patterns in sphinx and nikola configurations"""

    md = "md"
    ipynb = "ipynb"
    html = "html"
    rst = "rst"


class BaseSite(OpenModel):
    git: _git.Git = None
    gh: _github.Github = None
    sphinx: _sphinx.Sphinx = None
    blog: _blog.Blog = None

    def __post_init__(self):
        self.gh = _github.Github(parent=self, id=self.id)
        self.git = _git.Git(parent=self)
        self.sphinx = _sphinx.Sphinx(parent=self)
        self.blog = _blog.Blog(parent=self)


class Site(BaseSite):
    """a model for site wide configuration data

    the site wide configuration is often shared across many build systems.
    the site class helps sharing this information across systems.
    """

    id: str = Field(..., description="a unique project descriptor: org/repo or url")
    title: str = Field(None, description="blog title")
    data_: dict = Field(default_factory=dict, description="custom data for later use")
    description: str = Field(None, description="a description of the site")
    formats: List[Format] = Field(default_factory=lambda: [".ipynb", ".md"])
    posts: List = Field(default_factory=list)
    pages: List = Field(default_factory=list)

    def __post_init__(self):
        super().__post_init__()
