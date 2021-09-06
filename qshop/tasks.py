"""doit tasks for configuring, linting, and building documentation"""

from pathlib import Path
from shutil import rmtree

from doit.task import clean_targets, dict_to_task
from doit.cmd_base import TaskLoader2
from pydantic import Field

from . import ClosedModel

# from .settings import DOIT_CONFIG, Settings

# SETTINGS = Settings()
# SETTINGS.set_site("Quansight/media")


class Task(ClosedModel):
    file_dep: list = None
    actions: list = Field(default_factory=list)
    task_dep: list = None
    targets: list = None
    cleanup: list = None
    uptodate: list = None
    doc: str
    name: str

    def get_task(self):
        return dict_to_task(self.dict())


def clean_nikola_output():
    rmtree(SETTINGS.output_dir)


def task_jb_config():
    """generate a jupyter book configuration file"""

    sphinx = SETTINGS.site.sphinx

    def write():
        Path(sphinx.config).write_text(sphinx.get_config().yaml())

    return dict(
        actions=[write],
        targets=[sphinx.config],
        clean=[clean_targets],
    )


def task_sphinx_config():
    """generate a sphinx and nikola configuration file"""
    sphinx = SETTINGS.site.sphinx
    return dict(
        file_dep=[SETTINGS.cwd / sphinx.config],
        actions=[
            f"jb config sphinx . --toc {sphinx.toc} --config {sphinx.site_config} > {sphinx.conf}"
        ],
        targets=[sphinx.conf],
        clean=[clean_targets],
    )


def task_nikola_build():
    """build the nikola docs"""
    sphinx = SETTINGS.site.sphinx

    return dict(
        file_dep=[sphinx.conf],
        actions=["nikola build"],
        targets=[SETTINGS.output_dir / "index.html"],
        clean=[clean_nikola_output],
    )


def task_sphinx_html():
    """build the sphinx html docs"""
    sphinx = SETTINGS.site.sphinx
    return dict(
        file_dep=[sphinx.conf, sphinx.toc],
        actions=[f"sphinx-build . {SETTINGS.output_dir / 'docs' }"],
        targets=[SETTINGS.output_dir / "docs" / "index.html"],
    )
