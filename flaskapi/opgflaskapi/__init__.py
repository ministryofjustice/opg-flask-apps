from flask import Flask
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from .healthcheck_blueprint import healthcheck_blueprint
from .database import Database


def create_flask_app(name: str, database_uri: str = None, connect_args={}) -> Flask:
    app = Flask(name)
    if database_uri is not None:
        app.database = Database(database_uri, connect_args)

    app.register_blueprint(healthcheck_blueprint)

    xray_recorder.configure(service=f"{name} Flask Rest API")
    XRayMiddleware(app, xray_recorder)

    return app
