# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask
from flask_cors import CORS
import v2


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v2.bp,
        url_prefix='/v2')
    return app

if __name__ == '__main__':
    app = create_app()
    CORS(app, supports_credentials = True)
    app.run(debug=True,port = 5000)
