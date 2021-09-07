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


class MarkdownFlavors(Enum):
    markdown = "markdown"
    commonmark = "commonmark"
    myst = "myst"


class BaseSite(OpenModel):
    git: _git.Git = None
    gh: _github.Github = None
    sphinx: _sphinx.Sphinx = None
    blog: _blog.Blog = None
    md_flavor: MarkdownFlavors = "myst"

    def __post_init__(self):
        self.git = _git.Git(parent=self)
        self.gh = _github.Github(parent=self)
        self.sphinx = _sphinx.Sphinx(parent=self)
        self.blog = _blog.Blog(parent=self)


class Site(BaseSite):
    """a model for site wide configuration data

    the site wide configuration is often shared across many build systems.
    the site class helps sharing this information across systems.
    """

    title: str = Field(None, description="blog title")
    data_: dict = Field(default_factory=dict, description="custom data for later use")
    description: str = Field(None, description="a description of the site")
    formats: List[Format] = Field(default_factory=lambda: [".ipynb", ".md"])
    build: Path = Path("output")
    posts: List = Field(default_factory=list)
    pages: List = Field(default_factory=list)
