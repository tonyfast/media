"""configuring, linting, and building docs"""
__version__ = "0.0.1"


def load_ipython_extension(shell):
    """qshop is an ipython magic of doit tasks, all of the tasks are available through the doit magic"""
    import doit

    doit.load_ipython_extension(shell)
    from . import tasks

    shell.user_ns.update(
        (k, v) for k, v in vars(tasks).items() if k.startswith("task_")
    )


def unload_ipython_extension(shell):
    pass
