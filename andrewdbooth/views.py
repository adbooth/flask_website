# andrewdbooth/views.py

from andrewdbooth import app
from flask import redirect, render_template, url_for

@app.route('/')
def index():
    return render_template('home.html', content_page_names=app.config['CONTENT_PAGE_NAMES'])

@app.route('/post')
@app.route('/post/<postname>')
def post():
    return 'post here'
