from uritemplate import URITemplate as _URITemplate


class UriTemplate(_URITemplate):
    def expand(self, *args, **kwargs):
        return Url(super().expand(*args, **kwargs))

    __call__ = expand


class Url(str):
    def get(self, cache=True, **kwargs):
        import os

        import requests

        token = os.getenv("ACCESS_TOKEN")

        if token:
            kwargs.setdefault("headers", dict())
            kwargs["headers"].update(Authorization=f"token {token}")

        if cache:
            try:
                import requests_cache

                requests_cache.install_cache(".qshop")
            except ModuleNotFoundError:
                pass
        return requests.get(self, **kwargs)


GH = UriTemplate("https://github.com{/org}{/repo}")
ORG = UriTemplate("https://api.github.com/orgs{/org}")
REPO = UriTemplate("https://api.github.com/repos{/org}{/repo}")
GH_PAGES = UriTemplate("https://{org}.github.io{/repo}")
