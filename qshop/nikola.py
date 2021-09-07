"""pydantic models for nikola"""


from datetime import datetime
from functools import partial
from pathlib import Path
from typing import List, Optional

from pydantic import AnyUrl, Field

from . import ClosedModel

POSTS = dict(en="posts")


class Options(ClosedModel):
    author: str
    data: Path
    filters: List
    hidetitle: bool = False
    nocomments: bool = False
    updated: datetime
    ADDITIONAL_METADATA: dict


# required metadata
# optional metadata


class Metadata(ClosedModel):
    title: str
    slug: str
    date: datetime
    tags: str
    has_math: bool = False
    category: str = None
    description: None
    type: str  # probably enum


class Nikola(ClosedModel):
    BLOG_AUTHOR: str
    BLOG_TITLE: str
    SITE_URL: Optional[str]
    BLOG_EMAIL: Optional[str]
    BLOG_DESCRIPTION: str
    DEFAULT_LANG: str = "en"
    POSTS: list = Field(
        default_factory=partial(
            list,
            (
                ("docs/mmxxi/*.rst", POSTS, "post.tmpl"),
                ("docs/mmxxi/*.md", POSTS, "post.tmpl"),
                ("docs/mmxxi/*.ipynb", POSTS, "post.tmpl"),
            ),
        )
    )
    PAGES: list = Field(default_factory=list)
    INDEX_TEASERS: bool = True
    EXTRA_PLUGINS_DIRS: list = None
    COMPILERS: dict = Field(default_factory=dict)

    def __post_init__(self):
        from . import nikola

        self.EXTRA_PLUGINS_DIRS = [str(Path(nikola.__file__).parent / "plugins")]
