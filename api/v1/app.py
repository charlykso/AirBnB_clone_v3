#!/usr/bin/python3
"""
the api file
"""

from os import environ
<<<<<<< HEAD
from flask import Flask
from models import storage
from api.v1.views import app_views
=======
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
>>>>>>> storage_get_count


app = Flask(__name__)
app.register_blueprint(app_views)
<<<<<<< HEAD
=======
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
>>>>>>> storage_get_count


@app.teardown_appcontext
def close_dataBase(e):
<<<<<<< HEAD
    """tear down app context"""
    
    storage.close()


if __name__ == '__main__':
    host=environ.get('HBNB_API_HOST')
    port=environ.get('HBNB_API_PORT')
=======
    """
    tear down app context
    """
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """
    404 route
    """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
>>>>>>> storage_get_count
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True, debug=True)
