"""models foor using information from a git repository"""

from typing import Any

from pydantic import Field

from . import OpenModel, Path


class Git(OpenModel):
    """a class containing local repository information."""

    repo: Any = Field(None, description="a python-git repository object")
    url: Any = Field(None, description="url to the git remote")
    org: str = Field(None, description="organization name")
    branch: str = Field(None, description="active branch name")
    name: str = Field(None, description="repo name")
    ignore: Any = Field(
        None, description="a pathspec representation of the gitignore")

    def set_branch(self):
        self.branch = self.repo.active_branch.name

    def set_repo(self):
        import git

        self.repo = git.Repo()

    def set_url(self):
        self.url = self.repo.git.execute(
            f"git config --get remote.origin.url".split())
        if self.url.endswith(".git"):
            self.url = self.url[:-4]

        _, self.org, self.name = self.url.rsplit("/", 2)

    def set_gitignore(self):
        ignore = Path(".gitignore")
        if ignore.exists():
            import pathspec

            self.ignore = pathspec.PathSpec.from_lines(
                pathspec.GitIgnorePattern, ignore.read_text().splitlines()
            )

    def __post_init__(self):
        self.set_repo()
        self.set_branch()
        self.set_url()
        self.set_gitignore()
