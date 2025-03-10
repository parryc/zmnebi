# from git import Repo
# import os
import markdown
import codecs
from bracket_table.bracket_table import BracketTable


def get_html(filepath):
    # repo = Repo(os.getcwd())
    # if host == "zmnebi.com":
    #     repo = Repo("/srv/data/vcs/git/default.git")
    #     folder = os.path.join("templates", "zmnebi")
    # else:
    #     repo = Repo(os.getcwd())
    #     folder = os.path.join(os.getcwd(), "templates", "zmnebi")
    # filepath = os.path.join(current_app.root_path, "templates", page)
    input_file = codecs.open(filepath, mode="r", encoding="utf-8")
    text = input_file.read()
    # time = repo.git.log("-n 1", "--format=%ci", "--", filepath)
    # time = " ".join(time.split(" ")[0:2])
    # text = (
    #     "_Last updated {0}_\n".format(time) + "<a href='/rss'>RSS feed</a>\n\n" + text
    # )
    return markdown.markdown(
        text,
        extensions=[
            "markdown.extensions.nl2br",
            "markdown.extensions.toc",
            "markdown.extensions.tables",
            "markdown.extensions.def_list",
            "markdown.extensions.abbr",
            "markdown.extensions.footnotes",
        ],
    )


def md_to_html(text):
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