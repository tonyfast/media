from doit.cmd_base import ModuleTaskLoader
from doit.doit_cmd import DoitMain
import sys

if __name__ == "__main__":
    from . import tasks

    try:
        from rich import print
        import builtins

        builtins.print = print
    except ModuleNotFoundError:
        pass
    sys.exit(DoitMain(ModuleTaskLoader(tasks)).run(sys.argv[1:]))
