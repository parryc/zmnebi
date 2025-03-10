import codecs
import os
from format import get_html, md_to_html
from jinja2 import Environment, PackageLoader, select_autoescape

cwd = os.getcwd()
env = Environment(
    loader=PackageLoader("pages"),
    autoescape=select_autoescape()
)
template = env.get_template("post.html")
pages = os.path.join(cwd, "pages")
dist = os.path.join(cwd, "dist")


for page in os.scandir(pages):
    if page.name.endswith(".md"):
        input_file = codecs.open(page.path, mode="r", encoding="utf-8")
        text = input_file.read()
        out_file = page.name.replace('.md', '')
        with open(os.path.join(dist, f'{out_file}.html'), 'w') as out:
            data = {'html': md_to_html(text), 't': 'Georgian Verbs | ქართული ზმნები'}
            html = template.render(**data)
            print(html, file=out)


# with open(filepath) as f:
#     with open(dist, 'a') as out:
#         data = yaml.safe_load(f)
#         print(data)
#         data['notes'] = md_to_html(data['notes'])
#         template = env.get_template("designers.html")
#         html = template.render(**data)
#         print(html, file=out)