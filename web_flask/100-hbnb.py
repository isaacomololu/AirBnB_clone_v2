#!/usr/bin/python3
"""Script that runs an app with Flask framework
The application listens on 0.0.0.0, port 5000.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Close the storage session after each request."""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays the main HBnB HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")

    return render_template("100-hbnb.html",
                           states=states, amenities=amenities,
                           places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
