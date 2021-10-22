from nox import session


@session(reuse_venv=True)
def build_docs(session):
    session.install("git+https://github.com/tonyfast/qpub@new")
    session.install("nikola", "notebook")
    session.run("qpub", "blog:metadata")
    session.run("qpub", "blog:configure")
    session.run("nikola", "build")
