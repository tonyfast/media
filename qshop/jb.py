"""models for jupyter book"""

from enum import Enum
from functools import partial
from typing import ForwardRef, List, Optional, Union

from pydantic import AnyUrl, Field, FilePath

from . import ClosedModel, nikola


class JupyterBookFormat(Enum):
    jb_book = "jb-book"
    jb_article = "jb-article"


class Entry(ClosedModel):
    file: Optional[Union[str, FilePath]]
    glob: Optional[str]
    url: Optional[AnyUrl]
    title: Optional[str]
    sections: Optional[ForwardRef("Entry")]


Entry.update_forward_refs()


class Chapter(ClosedModel):
    caption: Optional[str]
    chapters: Optional[List[Entry]]


class Content(ClosedModel):
    chapters: Optional[List[Entry]]
    parts: Optional[List[Chapter]]
    sections: Optional[List[Entry]]


class Toc(Content):
    format: JupyterBookFormat = "jb-book"
    root: str = "readme"

    def append(self, section):
        self.sections = self.sections or []
        self.sections.append(section)
        return self


class EXECUTE(Enum):
    auto = "auto"
    force = "force"
    cache = "cache"
    off = "off"


class STDERR(Enum):
    show = "show"
    remove = "remove"
    remove_warn = "remove-warn"
    warn = "warn"
    error = "error"
    severe = "severe"


class TEX(Enum):
    pdflatex = "pdflatex"
    xelatex = "xelatex"
    luatex = "luatex"
    platex = "platex"
    uplatex = "uplatex"


class Comments(ClosedModel):
    hypothesis: bool = False
    utterances: bool = False


class JupyterBookConfig(ClosedModel):
    """model for the jupyter book configuration file
    that contains all of the documentation building information.

    Notes
    -----

    it configures:
    * sphinx
    * latex
    * nikola

        both nikola and sphinx use the conf.py convention. nikola using capital letters
        for variables names while sphinx uses lowercase. because of these differences we
        can configure documentation for both in the same file, and share configuration
        metadata.

    Note
    ----

    the descriptions were taken from the jb docs https://jupyterbook.org/customize/config.html

    """

    class Execute(ClosedModel):
        """notebook execution settings"""

        execute_notebooks: EXECUTE = Field(
            "off", description="jupyter book execution mode; off by default"
        )
        cache: str = Field(
            "",
            description="A path to the jupyter cache that will be used to store execution artifacts. Defaults to `_build/.jupyter_cache/`",
        )
        exclude_patterns: List[str] = Field(
            default_factory=list,
            description="A list of patterns to *skip* in execution (e.g. a notebook that takes a really long time)",
        )
        timeout: float = Field(
            30,
            description="The maximum time (in seconds) each notebook cell is allowed to run.",
        )
        run_in_temp: bool = Field(
            False,
            description="""If `True`, then a temporary directory will be created and used as the command working directory (cwd), 
            otherwise the notebook's parent directory will be the cwd.""",
        )
        allow_errors: bool = Field(
            True,
            description="when a code cell raises an error the execution is stopped, otherwise all cells are always run. default is false so docs are created",
        )
        stderr_output: STDERR = Field(
            "show",
            description="the mode to show the stderr output in; the default is show for debugging.",
        )

    class Parse(ClosedModel):
        myst_enable_extensions: List[str] = Field(
            default_factory=lambda: "linkify substitution dollarmath colon_fence".split(),
            description="default extensions to enable in the myst parser. See https://myst-parser.readthedocs.io/en/latest/using/syntax-optional.html",
        )
        myst_url_schemes: List[str] = Field(
            default_factory=lambda: "mailto http https".split(),
            description="URI schemes that will be recognised as external URLs in Markdown links",
        )

    class Html(ClosedModel):
        favicon: str = ""
        use_edit_page_button: bool = False
        use_repository_button: Union[bool, str] = False
        use_issues_button: bool = False
        use_multitoc_numbering: bool = True
        extra_navbar: str = ""
        extra_footer: str = ""
        google_analytics_id: str = ""
        home_page_in_navbar: bool = True
        baseurl: str = ""
        comments: Optional[Comments] = Field(default_factory=Comments)

    class Latex(ClosedModel):
        latex_engine: TEX = "pdflatex"
        use_jupyterbook_latex: bool = False

    class Buttons(ClosedModel):
        pass

    class Sphinx(ClosedModel):
        extra_extensions: Optional[list]
        local_extensions: Optional[list]
        config: nikola.Nikola = Field(
            default_factory=nikola.Nikola,
            description="extra sphinx configuration values",
        )

    class Repository(ClosedModel):
        pass

    title: Optional[str]
    author: Optional[str]
    copyright: Optional[str]
    logo: Optional[str]
    exclude_patterns: List = Field(default_factory=partial(list, [".nox", "_build"]))
    only_build_toc_files: bool = False

    execute: Optional[Execute] = Field(default_factory=Execute)
    parse: Optional[Parse] = Field(default_factory=Parse)
    html: Optional[Html] = Field(default_factory=Html)
    repository: Optional[Repository] = Field(default_factory=Repository)
    launch_buttons: Optional[Buttons] = Field(default_factory=Buttons)
    latex: Optional[Latex] = Field(default_factory=Latex)
    sphinx: Sphinx = Field(default_factory=Sphinx)
