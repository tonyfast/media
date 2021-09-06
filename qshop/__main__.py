from . import Site
from doit.cmd_base import TaskLoader2
from doit.doit_cmd import DoitMain
import sys
from pydantic import Field
from typing import List, Any


class Tasks(Site, TaskLoader2):
    cmd_names: List = Field(default_factory=list)
    config: Any = None

    def __init__(self, *args, **kwargs):
        Site.__init__(self, *args, **kwargs)
        TaskLoader2.__init__(self)
        self.__post_init__()

    def load_doit_config(self):
        return dict(verbosity=2, backend="json")

    def load_tasks(self, cmd, pos_args):
        return self.sphinx.load_tasks(cmd, pos_args)


if __name__ == "__main__":
    sys.exit(DoitMain(Tasks(id="Quansight/media")).run(sys.argv[1:]))
