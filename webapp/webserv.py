#!/usr/bin/env python3
"""
Map-based discovery of Boojum Technical Reports Front End
"""

import flask
from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader(searchpath="%s/templates" % os.path.dirname((os.path.realpath(__file__)))), trim_blocks=True)

app = flask.Flask(__name__)

@app.route("/")
def index():
    """ Serve the landing page """
    template = env.get_template('index.html')
    return(template.render())

if __name__ == '__main__':
    app.debug = True
    app.run()
