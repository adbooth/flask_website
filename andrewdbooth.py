""" andrewdbooth.py
This creates path strings for use when reading content files
Also defines Flask view functions
"""
from flask import Flask, json, Markup, render_template, g
from markdown import markdown
import os

# Start application
app = Flask(__name__)
app.debug = True

# Scene data structure
STANDARD_SCENES = ['home', 'projects', 'resume']

# Path shortcut strings
PATHS = {}
PATHS['root'] = os.path.dirname(os.path.abspath(__file__))
PATHS['scenes'] = os.path.join(PATHS['root'], 'static/scenes')
for standard_scene in STANDARD_SCENES:
    PATHS[standard_scene] = os.path.join(PATHS['scenes'], standard_scene)

@app.route('/')
def theater():
    """ Serves the theater view from the index URL """
    # Store scene list on global object
    g.standard_scenes = STANDARD_SCENES

    # Render markdown from about ('home.md') file and store on global object
    with open(os.path.join(PATHS['home'], 'home.md')) as home_file:
        g.home = Markup(markdown(home_file.read()))

    # Load project index data structure into global object
    with open(os.path.join(PATHS['projects'],'project_index.json')) as index_file:
        g.project_index = json.load(index_file)['project_index']

    # Create scenes dict on global object and populate with standard scenes...
    g.scenes = {}
    for scene in g.standard_scenes:
        g.scenes[scene] = Markup(render_template(scene + '.html'))
    # ...and project scenes
    for filename in os.listdir(PATHS['projects']):
        if filename.endswith('.md'):
            with open(os.path.join(PATHS['projects'], filename)) as project_file:
                g.scenes[filename.replace('.md', '')] = Markup(markdown(project_file.read()))

    # Render page
    return render_template('theater.html')

@app.route('/clock')
def clock():
    """ Serves the clock view from URL '/clock' """
    return render_template('clock.html')

@app.route('/unipagestats')
def edustats():
    """ Serves .edu stats view from URL '/unipagestats' """
    g.schools = {}
    # g.schoolstring = open(os.path.join(PATHS['scenes'], 'unipagestats/schools.jl')).read()
    with open(os.path.join(PATHS['scenes'], 'unipagestats/schools.jl')) as school_file:
        for line in school_file.readlines():
            school = json.loads(line)
            g.schools[school['name']] = school
            # g.schools.append(line)

    return render_template('unipagestats.html')
