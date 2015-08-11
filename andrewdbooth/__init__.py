# andrewdbooth/__init__.py

from flask import Flask, json, Markup
from markdown import markdown
import os

# Start application
app = Flask(__name__)
app.config.from_object('config')

# Make path shortcuts
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
APP_CONTENT = os.path.join(APP_STATIC, 'content')
APP_PROJECT_FILES = os.path.join(APP_CONTENT, 'project_files')

# Make content object
content = {}
content['page_name_list'] = app.config['CONTENT_PAGE_NAMES']

# Make about object for content object
with open(os.path.join(APP_CONTENT, 'about.md')) as f:
    content['about'] = Markup(markdown(f.read()))

# Make blog object for content object
content['blog'] = 'blog here'

# Make projects object for content object
with open(os.path.join(APP_CONTENT, 'projects.json')) as f:
    content['projects'] = json.load(f)['projects']

content['project_files'] = {}
for filename in os.listdir(APP_PROJECT_FILES):
    with open(os.path.join(APP_PROJECT_FILES, filename)) as f:
        content['project_files'][filename.replace('.md', '')] = Markup(markdown(f.read()))

import andrewdbooth.views
