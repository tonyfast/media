from functools import partial
from . import BaseModel, NonNull
from .nikola import Nikola
from pydantic import FilePath, AnyUrl, Field
from typing import Optional, Union, ForwardRef, List
from enum import Enum


class FORMAT(Enum):
    jb_book = "jb-book"
    jb_article = "jb-article"


class Entry(NonNull):
    file: Optional[Union[str, FilePath]]
    glob: Optional[str]
    url: Optional[AnyUrl]
    title: Optional[str]
    sections: Optional[ForwardRef("Entry")]


Entry.update_forward_refs()


class Chapter(NonNull):
    caption: Optional[str]
    chapters: Optional[List[Entry]]


class Content(NonNull):
    chapters: Optional[List[Entry]]
    parts: Optional[List[Chapter]]
    sections: Optional[List[Entry]]


class Toc(Content):
    format: FORMAT = "jb-book"
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


class StdErr(Enum):
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


class Comments(BaseModel):
    hypothesis: bool = False
    utterances: bool = False


class Config(NonNull):
    class Execute(BaseModel):
        execute_notebooks: EXECUTE = "off"
        cache: str = ""
        exclude_patterns: List[str] = Field(default_factory=list)
        timeout: float = 30
        run_in_temp: bool = True
        allow_errors: bool = True

    class Parse(BaseModel):
        myst_enable_extensions: List[str] = Field(
            default_factory=lambda: "linkify substitution dollarmath colon_fence".split()
        )
        myst_url_schemes: List[str] = Field(
            default_factory=lambda: "mailto http https".split()
        )

    class Html(BaseModel):
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

    class Latex(BaseModel):
        latex_engine: TEX = "pdflatex"
        use_jupyterbook_latex: bool = False

    class Buttons(BaseModel):
        pass

    class Sphinx(NonNull):
        extra_extensions: Optional[list]
        local_extensions: Optional[list]
        config: Nikola = Field(default_factory=Nikola)

    class Repository(BaseModel):
        pass

    title: Optional[str]
    author: Optional[str]
    copyright: Optional[str]
    logo: Optional[str]
    exclude_patterns: List = Field(default_factory=partial(list, [".nox", "_build"]))
    only_build_toc_files: bool = False
    stderr_output: Optional[StdErr]

    execute: Optional[Execute] = Field(default_factory=Execute)
    parse: Optional[Parse] = Field(default_factory=Parse)
    html: Optional[Html] = Field(default_factory=Html)
    repository: Optional[Repository] = Field(default_factory=Repository)
    launch_buttons: Optional[Buttons] = Field(default_factory=Buttons)
    latex: Optional[Latex] = Field(default_factory=Latex)
    sphinx: Sphinx = Field(default_factory=Sphinx)
