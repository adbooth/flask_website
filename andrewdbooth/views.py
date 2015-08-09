# andrewdbooth/views.py

from andrewdbooth import app
from flask import redirect, render_template, url_for

content = {}
# content['page_name_list'] = app.config['CONTENT_PAGE_NAMES']
content['page_name_list'] = []
for name in app.config['CONTENT_PAGE_NAMES']:
    content['page_name_list'].append(name)
    content[name] = app.config[name.upper()]

@app.route('/')
def index():
    return render_template('index.html', content=content)

@app.route('/post')
@app.route('/post/<postname>')
def post():
    return 'post here'
