from git import Repo
import os
import markdown
from bracket_table.bracket_table import BracketTable


def md_to_html(text, path):
    repo = Repo(os.getcwd())
    time = repo.git.log("-n 1", "--format=%ci", "--", path)
    time = " ".join(time.split(" ")[0:2])
    text = (
        "_Last updated {0}_\n\n".format(time) + text
    )
    return markdown.markdown(
        text,
        extensions=[
            "markdown.extensions.nl2br",
            "markdown.extensions.toc",
            "markdown.extensions.tables",
            "markdown.extensions.def_list",
            "markdown.extensions.abbr",
            "markdown.extensions.footnotes",
            BracketTable(),
            "doctor_leipzig.doctor_leipzig",
            "examples_md.examples",
        ],
    )