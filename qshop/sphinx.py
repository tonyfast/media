from doit.task import clean_targets

from . import OpenModel, Path, jb, nikola


class Sphinx(OpenModel):
    """sphinx configuration is driven through jupyter book.

    nikola is also considered as part of sphinx configuration.
    we double dip with jupyter books configuration file to configure
    nikola variables in conf.py"""

    config: Path = Path("config.yml")
    toc: Path = Path("toc.yml")
    conf: Path = Path("conf.py")

    def get_config(self):
        """generate the jupyter book configuration file for the site."""
        parent = self.parent

        parent.gh.get_repo()
        repo = parent.gh.data[parent.gh.get_repo_url()]

        return jb.JupyterBookConfig(
            title=parent.title,
            author=parent.gh.org,
            sphinx=jb.JupyterBookConfig.Sphinx(
                config=nikola.Nikola(
                    BLOG_AUTHOR=parent.gh.org,
                    BLOG_TITLE=repo["description"],
                    SITE_URL=repo["html_url"],
                    BLOG_DESCRIPTION=repo["description"],
                    COMPILERS=dict(
                        {
                            self.parent.md_flavor: [".md", ".mdown", ".markdown"],
                        },
                        rest=[".rst"],
                        ipynb=[".ipynb"],
                        html=[".html", ".htm"],
                    ),
                )
            ),
        )

    def set_config(self):
        def update():
            import yaml

            self.config.write_text(
                yaml.safe_dump(self.get_config().dict(), default_flow_style=False)
            )

        return Task(
            name="jb-config",
            actions=[update],
            targets=[self.config],
            doc="""write to jupyter books configuration file""",
        )

    def set_conf_py(self):
        """write to sphinx/nikola's configuration file"""

        return Task(
            name="conf-py",
            file_dep=[self.config],
            doc="translate jupyter book to sphinx configuration",
            actions=[
                f"jb config sphinx . --toc {self.toc} --config {self.config} > {self.conf}"
            ],
            targets=[self.conf],
            clean=[clean_targets],
        )
