#!/usr/bin/python3
""" flask module """
from models.state import State
from flask import Flask, render_template, request, session
from models import storage


# create a Flask application object
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ get all states """
    states = storage.all(cls=State)
    return render_template('7-states_list.html', states=states.values())


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
