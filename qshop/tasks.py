"""doit tasks for configuring, linting, and building documentation"""

from .settings import SETTINGS, DOIT_CONFIG
from pathlib import Path
from shutil import rmtree
from doit.task import clean_targets


def clean_nikola_output():
    rmtree(SETTINGS.output_dir)


def task_jb_config():
    """generate a jupyter book configuration file"""

    def write():
        site = SETTINGS.site.set_site(project="Quansight/media")
        Path(SETTINGS.cwd / SETTINGS.site_config).write_text(
            site.from_github().to_jb().yaml()
        )

    return dict(
        actions=[write],
        targets=[SETTINGS.cwd / SETTINGS.site_config],
        clean=[clean_targets],
    )


def task_sphinx_config():
    """generate a sphinx and nikola configuration file"""
    return dict(
        file_dep=[SETTINGS.cwd / SETTINGS.site_config],
        actions=[
            f"jb config sphinx . --toc {SETTINGS.toc} --config {SETTINGS.toc} > {SETTINGS.conf}"
        ],
        targets=[SETTINGS.conf],
        clean=[clean_targets],
    )


def task_nikola_build():
    """build the nikola docs"""
    return dict(
        file_dep=[SETTINGS.conf],
        actions=["nikola build"],
        targets=[SETTINGS.output_dir / "index.html"],
        clean=[clean_nikola_output],
    )


def task_sphinx_html():
    """build the sphinx html docs"""
    return dict(
        file_dep=[SETTINGS.conf],
        actions=[f"sphinx-build . {SETTINGS.output_dir / 'docs' }"],
        targets=[SETTINGS.output_dir / "docs" / "index.html"],
    )
