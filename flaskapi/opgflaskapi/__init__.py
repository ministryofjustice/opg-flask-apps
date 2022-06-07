from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

# TODO pass in postgres creds,  name becomes a config obj passed in after extracting from env,  with db type
# exceptions if not passed in, tests of this   possibly use Config library
# possibly check env vars if not passed in


def create_flask_app(name: str, dbconnstr: str) -> Flask: 
    app = Flask(name)
    app.config['SQLALCHEMY_DATABASE_URI'] = dbconnstr
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.db = SQLAlchemy(app)
    return Flask(name)
