from models.state import State
from models.city import City
from flask import Flask, render_template
from models import storage


# create a Flask application object
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id=""):
    states = storage.all(cls=State)
    cities = storage.all(cls=City)
    return render_template('9-states.html',
                           states=states.values(),
                           cities=cities.values(), id=id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
