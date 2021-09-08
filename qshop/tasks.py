"""doit tasks for configuring, linting, and building documentation"""
from contextlib import contextmanager
from pathlib import Path
from shutil import rmtree

from doit.cmd_base import TaskLoader2
from doit.task import clean_targets, dict_to_task
from pydantic import Field

from . import ClosedModel, Site

DOIT_CONFIG = dict(verbosity=2, dep_file=".qshop-doit")

self = Site()


def clean_nikola_output():
    if self.build.exists():
        rmtree(self.build)


def task_jb_config():
    """generate a jupyter book configuration file"""

    def write():
        Path(self.sphinx.config).write_text(self.sphinx.get_config().yaml())

    return dict(
        actions=[write],
        targets=[self.sphinx.config],
        clean=[clean_targets],
    )


def task_sphinx_config():
    """generate a sphinx and nikola configuration file"""
    return dict(
        file_dep=[self.sphinx.config],
        actions=[
            f"jb config sphinx . --toc {self.sphinx.toc} --config {self.sphinx.config} > {self.sphinx.conf}",
        ],
        targets=[self.sphinx.conf],
        clean=[clean_targets],
    )


def task_nikola_build():
    """build the nikola docs"""
    return dict(
        file_dep=[self.sphinx.conf],
        actions=["nikola build"],
        targets=[self.build / "index.html"],
        clean=[clean_nikola_output],
    )


def task_sphinx_html():
    """build the sphinx html docs"""
    return dict(
        file_dep=[self.sphinx.conf, self.sphinx.toc],
        actions=[f"sphinx-build . {self.build / 'dev' }", "touch .nojekyll"],
        targets=[self.build / "dev" / "index.html", self.build / ".nojekyll"],
    )
