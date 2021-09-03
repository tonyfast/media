from pydantic import BaseModel


def get_url(url):
    import requests
    import requests_cache

    requests_cache.install_cache(".qshop")
    return requests.get(url)


class Markdown(str):
    def _repr_markdown_(self):
        return self


class BaseModel(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self, "__post_init__"):
            self.__post_init__()

    def yaml(self):
        import yaml

        return yaml.safe_dump(self.dict(), default_flow_style=False)


class NonNull(BaseModel):
    def dict(self, *args, **kwargs):
        return {k: v for k, v in super().dict(*args, **kwargs).items() if v is not None}
