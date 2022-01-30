#!/usr/bin/python3
""" flask module """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome():
    """ Return hello HBNBH"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def simple_print():
    """ return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Return C is and input """
    return 'C %s' % text.replace("_", " ")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
