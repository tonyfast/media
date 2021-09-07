from typing import Any, Dict

from pydantic import AnyUrl, Field

from . import OpenModel, urls


class Github(OpenModel):
    """a pydantic model for interactign with the github api"""

    org: str = Field(None, description="org name")
    name: str = Field(None, description="repo name")
    branch: str = Field(None, description="the active branch name")
    data: Dict[AnyUrl, Any] = Field(
        default_factory=dict,
        description="data returned from requests to the github api.",
    )
    cache: bool = Field(
        True, description="cache the api requests, requires requests_cache"
    )

    def __post_init__(self):
        self.org, self.name, self.branch = (
            self.parent.git.org,
            self.parent.git.name,
            self.parent.git.branch,
        )

    def get(self, url, **kwargs):
        url = urls.Url(url)
        if url not in self.data:
            response = url.get(self.cache, **kwargs)
            self.data.update({url: response.json()})
        return self.data[url]

    def get_repo_url(self):
        return urls.Url(urls.REPO.expand(org=self.org, repo=self.name))

    def get_repo(self, **kwargs):
        return self.get(self.get_repo_url())

    def get_org_url(self):
        return urls.Url(urls.ORG.expand(org=self.org))

    def get_org(self, **kwargs):
        return self.get(self.get_org_url())
