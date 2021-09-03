from qshop.models.nikola import Nikola
from typing import Any, List
from pydantic import BaseModel, Field

from pathlib import Path
from pydantic.networks import AnyUrl
import requests
from .. import urls
from . import jb, nikola, BaseModel, page
from . import NonNull


class Configs(BaseModel):
    conf: Path = "conf.py"
    toc: Path = "toc.yml"
    config: Path = "config.py"


class Site(NonNull):
    """a model for site wide configuration data

    the site wide configuration is often shared across many build systems.
    the site class helps sharing this information across systems.


    * conf.py/toc.yml/config.yml
    * pyproject.toml
    """

    class Urls(BaseModel):
        repo: AnyUrl
        org: AnyUrl
        pages: AnyUrl

    project: str
    title: str = None
    data_: dict = Field(default_factory=dict)
    org: str = None
    repo: str = None
    gh_api: str = None
    description: str = None

    configs: Configs = Field(default_factory=Configs)
    posts: List[str] = Field(default_factory=list)

    def __post_init__(self):
        assert "/" in self.project, "A pattern of org/repo was expected for project"
        self.org, _, self.repo = self.project.partition("/")
        self.gh_api = urls.REPO(org=self.org, repo=self.repo)

    def from_github(self):
        self.data_.update(self.gh_api.get().json())

        self.description = self.data_["description"]
        self.title = self.title or self.data_["name"]
        return self

    def to_jb(self):
        return jb.Config(
            title=self.title,
            author=self.org,
            sphinx=jb.Config.Sphinx(
                config=nikola.Nikola(
                    BLOG_AUTHOR=self.org,
                    BLOG_TITLE=self.title,
                    SITE_URL=self.data_["html_url"],
                    BLOG_DESCRIPTION=self.description,
                )
            ),
        )

    def discover(self):
        self.posts = [page.Page(path=x) for x in get_posts()]
        return self


def get_posts(config="conf.py"):
    import runpy

    files = []
    conf = runpy.run_path(config, run_name="tmp")
    for location, lang, tpl in conf["POSTS"]:
        files += get_files_in_dir(location)
    return files


def get_files_in_dir(location):
    path = Path(location)
    return list(path.parent.rglob(f"*{path.suffix}"))
