from typing import Any

from pydantic import BaseModel as _BaseModel


class BaseModel(_BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self, "__post_init__"):
            self.__post_init__()

    def dict(self, *args, **kwargs):
        return {
            k: v
            for k, v in super().dict(*args, **kwargs).items()
            if v is not None and k not in "parent"
        }


def get_url(url):
    import requests
    import requests_cache

    requests_cache.install_cache(".qshop")
    return requests.get(url)


class Markdown(str):
    def _repr_markdown_(self):
        return self


class OpenModel(BaseModel):
    """OpenModels are custom object oriented classes without an implict schema"""

    parent: Any = None


class ClosedModel(BaseModel):
    """OpenModels are custom object oriented classes with an implict schema (eg jupyterbook, pyproject)"""

    def yaml(self):
        import yaml

        return yaml.safe_dump(self.dict(), default_flow_style=False)

    def dict(self, *args, **kwargs):
        return {k: v for k, v in super().dict(*args, **kwargs).items() if v is not None}
