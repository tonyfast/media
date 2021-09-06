from typing import Any

from pydantic import AnyUrl, Field

from . import OpenModel, Path, urls


class Git(OpenModel):
    """a class containing local repository information."""

    repo: Any = Field(None, description="a python-git repository object")
    ignore: Any = Field(None, description="a pathspec representation of the gitignore")

    def __post_init__(self):
        import git

        self.repo = git.Repo()
        ignore = Path(".gitignore")
        if ignore.exists():
            import pathspec

            self.ignore = pathspec.PathSpec.from_lines(
                pathspec.GitIgnorePattern, ignore.read_text().splitlines()
            )
