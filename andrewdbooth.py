# andrewdbooth.py
from flask import Flask, json, Markup, render_template, g
from markdown import markdown
import os

# Start application
app = Flask(__name__)

# Scene data structure
standard_scenes = ['home', 'projects', 'resume']

# Path shortcut strings
paths = {}
paths['root'] = os.path.dirname(os.path.abspath(__file__))
paths['scenes'] = os.path.join(paths['root'], 'static/scenes')
for scene in standard_scenes:
    paths[scene] = os.path.join(paths['scenes'], scene)

# Serve page
@app.route('/')
def theater():
    # Store scene list on global object
    g.standard_scenes = standard_scenes

    # Render markdown from about ('home.md') file and store on global object
    with open(os.path.join(paths['home'], 'home.md')) as f:
        g.home = Markup(markdown(f.read()))

    # Load project index data structure into global object
    with open(os.path.join(paths['projects'], 'project_index.json')) as f:
        g.project_index = json.load(f)['project_index']

    # Create scenes dictionary on global object and populate with standard scenes...
    g.scenes = {}
    for scene in standard_scenes:
        g.scenes[scene] = Markup(render_template(scene + '.html'))
    # ...and project scenes
    for filename in os.listdir(paths['projects']):
        if filename.endswith('.md'):
            with open(os.path.join(paths['projects'], filename)) as f:
                g.scenes[filename.replace('.md', '')] = Markup(markdown(f.read()))

    # Render page
    return render_template('theater.html')

@app.route('/clock')
def clock():
    return render_template('clock.html')
