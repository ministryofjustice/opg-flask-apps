from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from .healthcheck_blueprint import healthcheck_blueprint 

def create_flask_app(name: str, dbconnstr : str = None) -> Flask: 
    app = Flask(name)
    if dbconnstr is not None:
        app.config['SQLALCHEMY_DATABASE_URI'] = dbconnstr
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.db = SQLAlchemy(app)

    app.register_blueprint(healthcheck_blueprint)

    xray_recorder.configure(service='Flask Rest API')
    XRayMiddleware(app, xray_recorder)

    return app
