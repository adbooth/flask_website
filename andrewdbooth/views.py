# andrewdbooth/views.py

from andrewdbooth import app, content
from flask import redirect, render_template, url_for

@app.route('/')
def index():
    return render_template('index.html', content=content)
