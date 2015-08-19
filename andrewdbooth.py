# andrewdbooth.py

from flask import Flask, json, Markup, render_template
from markdown import markdown
import os

# Start application
app = Flask(__name__)
app.config.from_object('config')

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

@app.route('/')
def index():
    return render_template('index.html', content=content)
