#!/usr/bin/env python3
"""
Boojum technical reports website flask implementation
"""

import flask
import os
from jinja2 import Environment, FileSystemLoader

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
