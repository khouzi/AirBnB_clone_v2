#!/usr/bin/python3
""" flask module """
from models.state import State
from models.city import City
from flask import Flask, render_template
from models import storage


# create a Flask application object
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ cities by states """
    states = storage.all(cls=State)
    cities = storage.all(cls=City)
    return render_template('8-cities_by_states.html',
                           states=states.values(),
                           cities=cities.values())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
