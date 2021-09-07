from typing import Any

from pydantic import AnyUrl, Field

from . import OpenModel, Path, urls


class Git(OpenModel):
    """a class containing local repository information."""

    repo: Any = Field(None, description="a python-git repository object")
    url: Any = Field(None, description="url to the git remote")
    org: str = Field(None, description="organization name")
    branch: str = Field(None, description="active branch name")
    name: str = Field(None, description="repo name")
    ignore: Any = Field(None, description="a pathspec representation of the gitignore")

    def __post_init__(self):
        import git

        self.repo = git.Repo()
        self.branch = self.repo.active_branch.name
        self.url = self.repo.git.execute(f"git config --get remote.origin.url".split())
        if self.url.endswith(".git"):
            self.url = self.url[:-4]

        _, self.org, self.name = self.url.rsplit("/", 2)

        ignore = Path(".gitignore")
        if ignore.exists():
            import pathspec

            self.ignore = pathspec.PathSpec.from_lines(
                pathspec.GitIgnorePattern, ignore.read_text().splitlines()
            )
