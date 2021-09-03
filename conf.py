BLOG_AUTHOR = "Quansight"
BLOG_DESCRIPTION = "A place for creating and publishing media. "
BLOG_TITLE = "media"
DEFAULT_LANG = "en"
PAGES = []
POSTS = [
    ["docs/mmxxi/*.rst", {"en": "posts"}, "post.tmpl"],
    ["docs/mmxxi/*.md", {"en": "posts"}, "post.tmpl"],
    ["docs/mmxxi/*.ipynb", {"en": "posts"}, "post.tmpl"],
]
SITE_URL = "https://github.com/Quansight/media"
author = "Quansight"
comments_config = {"hypothesis": False, "utterances": False}
copyright = "2021"
exclude_patterns = ["**.ipynb_checkpoints", ".DS_Store", ".nox", "Thumbs.db", "_build"]
execution_allow_errors = True
execution_excludepatterns = []
execution_in_temp = True
execution_timeout = 30
extensions = [
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "myst_nb",
    "jupyter_book",
    "sphinx_thebe",
    "sphinx_comments",
    "sphinx_external_toc",
    "sphinx.ext.intersphinx",
    "sphinx_panels",
    "sphinx_book_theme",
]
external_toc_exclude_missing = False
external_toc_path = "/home/tonyfast/Documents/media/_toc.yml"
html_add_permalinks = "¶"
html_baseurl = ""
html_favicon = ""
html_logo = ""
html_sourcelink_suffix = ""
html_theme = "sphinx_book_theme"
html_theme_options = {
    "search_bar_text": "Search this book...",
    "launch_buttons": {
        "notebook_interface": "classic",
        "binderhub_url": "https://mybinder.org",
        "jupyterhub_url": "",
        "thebe": False,
        "colab_url": "",
    },
    "path_to_docs": "",
    "repository_url": "https://github.com/executablebooks/jupyter-book",
    "repository_branch": "master",
    "google_analytics_id": "",
    "extra_navbar": "",
    "extra_footer": "",
    "home_page_in_toc": True,
    "use_repository_button": False,
    "use_edit_page_button": False,
    "use_issues_button": False,
}
html_title = "media"
jupyter_cache = ""
jupyter_execute_notebooks = "off"
language = None
latex_engine = "pdflatex"
myst_enable_extensions = ["linkify", "substitution", "dollarmath", "colon_fence"]
myst_url_schemes = ["mailto", "http", "https"]
nb_output_stderr = "show"
numfig = True
panels_add_bootstrap_css = False
pygments_style = "sphinx"
suppress_warnings = ["myst.domains"]
use_jupyterbook_latex = False
INDEX_TEASERS = True
