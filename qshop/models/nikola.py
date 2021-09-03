from pathlib import Path
from . import NonNull
from functools import partial
from pydantic import Field, AnyUrl
from typing import Optional, List
from datetime import datetime

POSTS = dict(en="posts")


class Options(NonNull):
    author: str
    data: Path
    filters: List
    hidetitle: bool = False
    nocomments: bool = False
    updated: datetime
    ADDITIONAL_METADATA: dict


class Metadata(NonNull):
    title: str
    slug: str
    date: datetime
    tags: str
    has_math: bool = False
    category: str = None
    description: None
    type: str  # probably enum


class Nikola(NonNull):
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
