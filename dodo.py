from qshop import Site
from pathlib import Path


def clean_plugins():
    plugins = Path("qshop/plugins")
    if plugins.exists():
        from shutil import rmtree

        rmtree(plugins)


def task_uml():
    return dict(actions=["pyreverse -o png -p qshop qshop"])


def task_plugins():
    plugins = "myst commonmark localsearch gallery_directive".split()

    return dict(
        actions=[f"nikola plugin -i {plugin}" for plugin in plugins]
        + ["mv plugins qshop"],
        targets=[f"qshop/plugins/{plugin}/{plugin}.plugin" for plugin in plugins],
        clean=[clean_plugins],
    )


def task_schema():
    """generate schema for main qshop models"""
    schema = Path("docs/schema")

    def export():
        from qshop.jb import JupyterBookConfig

        schema.mkdir(exist_ok=True, parents=True)
        (schema / "config.json").write_text(JupyterBookConfig.schema_json(indent=2))

    return dict(actions=[export], targets=[(schema / "config.json")])
