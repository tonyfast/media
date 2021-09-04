if __name__ == "__main__":
    from . import tasks

    import sys

    from doit.cmd_base import ModuleTaskLoader
    from doit.doit_cmd import DoitMain

    sys.exit(DoitMain(ModuleTaskLoader(tasks)).run(sys.argv[1:]))
