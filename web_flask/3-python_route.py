#!/usr/bin/python3
""" flask module """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome_route():
    """ Return hello HBNBH"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def simple_print_route():
    """ return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ Return C is and input """
    return 'C %s' % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    """ return Python is and input"""
    return 'Python %s' % text.replace("_", " ")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
