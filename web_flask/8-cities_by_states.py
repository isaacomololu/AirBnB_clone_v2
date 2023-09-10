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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of all states and related cities.
"""
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
