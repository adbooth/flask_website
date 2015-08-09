# config.py

from flask import json, Markup
from markdown import markdown
from os.path import join

DEBUG = True

static_path = 'andrewdbooth/static/'
content_path = join(static_path, 'content')

with open(join(content_path, 'content_page_names.json')) as f:
    CONTENT_PAGE_NAMES = json.load(f)['names']

with open(join(content_path, 'about.md')) as f:
    ABOUT = Markup(markdown(f.read()))

BLOG = 'blog here'
RESUME = 'resume here'
PROJECTS = 'projects here'
