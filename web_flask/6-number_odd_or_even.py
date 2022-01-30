#!/usr/bin/python3
""" flask module """
from flask import Flask, render_template
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
    """ return python is and input"""
    return 'python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ check if n is an int """
    return "%i is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """ return html page if n is integer """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def template_odd_or_even_route(n):
    """ return n is even or odd """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
