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
APP_IMAGE = os.path.join(APP_ROOT, 'img')

# Make content object
content = {}
content['page_name_list'] = app.config['CONTENT_PAGE_NAMES']

# Make about object for content object
with open(os.path.join(APP_CONTENT, 'about.md')) as f:
    content['about'] = Markup(markdown(f.read()))

# Make blog object for content object
content['blog'] = 'blog here'

# Make projects object for content object
# content['projects'] = {}
with open(os.path.join(APP_CONTENT, 'projects.json')) as f:
    content['projects'] = json.load(f)['projects']

import andrewdbooth.views
