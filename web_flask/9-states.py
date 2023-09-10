#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: display "HBNB"
    /c/<text>: Display 'C' followed by the value of <text>.
    /python/(<text>): Display python followed by the value of <text>.
    /number/<n>: Display "<n> is a number" if n is an integer.
    /number_template/<n>: Display a HTML page if n is an integer
    /number_odd_or_even/<n>: Display a HTML page if n is an integer.
    /states_list: display a HTML page
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """Close the storage session after each request."""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page with a list of all states.

    States are sorted by name.
    """
    return render_template('7-states_list.html', states=storage.all('State'))


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """Displays an HTML page with cities of state.<id>, if it exists."""
    for state in storage.all('State').values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
