from nox import session


@session(reuse_venv=True)
def run(session):
    session.install("-rrequirements.txt")
    session.install("-rrequirements-sphinx.txt")
    session.run(*"python -mqshop clean".split())
    session.run(*"python -mqshop --".split() + session.posargs)
