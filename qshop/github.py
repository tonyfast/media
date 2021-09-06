from typing import Any, Dict

from pydantic import AnyUrl, Field

from . import OpenModel, urls


class Github(OpenModel):
    """a pydantic model for interactign with the github api"""

    id: str = Field(..., description="a valid github identifier")
    org: str = Field(None, description="org name")
    repo: str = Field(None, description="repo name")
    data: Dict[AnyUrl, Any] = Field(
        default_factory=dict,
        description="data returned from requests to the github api.",
    )
    cache: bool = Field(
        True, description="cache the api requests, requires requests_cache"
    )

    def __post_init__(self):
        assert "/" in self.id, "A pattern of org/repo was expected for project or url"
        self.org, _, self.repo = self.id.partition("/")

    def get(self, url, **kwargs):
        url = urls.Url(url)
        response = url.get(self.cache, **kwargs)
        self.data.update({url: response.json()})
        return response

    def get_repo_url(self):
        return urls.Url(urls.REPO.expand(org=self.org, repo=self.repo))

    def get_repo(self, **kwargs):
        return self.get(self.get_repo_url())

    def get_org_url(self):
        return urls.Url(urls.ORG.expand(org=self.org))

    def get_org(self, **kwargs):
        return self.get(self.get_org_url())
