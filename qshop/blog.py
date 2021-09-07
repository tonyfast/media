from . import OpenModel, Path, page


class Blog(OpenModel):
    """manage and interact with blog content"""

    def discover(self):
        self.posts = [page.Page(path=x) for x in get_posts()]
        return self


def get_posts(config="conf.py"):
    import runpy

    files = []
    conf = runpy.run_path(config, run_name="tmp")
    for location, lang, tpl in conf["POSTS"]:
        files += get_files_in_dir(location)
    return files


def get_files_in_dir(location):
    path = Path(location)
    return list(path.parent.rglob(f"*{path.suffix}"))
