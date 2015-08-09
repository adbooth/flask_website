# andrewdbooth/__init__.py

from flask import Flask, Markup
from markdown import markdown
import os

# Start application
app = Flask(__name__)
app.config.from_object('config')

# Make path shortcuts
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
APP_CONTENT = os.path.join(APP_STATIC, 'content')

# Make content object
content = {}
content['page_name_list'] = app.config['CONTENT_PAGE_NAMES']

with open(os.path.join(APP_CONTENT, 'about.md')) as f:
    content['about'] = Markup(markdown(f.read()))

content['blog'] = 'blog here'
content['resume'] = 'resume here'
content['projects'] = APP_CONTENT

import andrewdbooth.views
