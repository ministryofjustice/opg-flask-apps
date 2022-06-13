from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
#from healthcheck_blueprint import healthcheck_blueprint

from flask import Blueprint
from flask import jsonify
import psycopg2
import logging

healthcheck_blueprint = Blueprint('healthcheck_blueprint', __name__)

@healthcheck_blueprint.route('/healthcheck')
def healthcheck():
    try:
        app.db.session.execute('SELECT 1')
    except Exception as e:
        logging.error('Failed to connect: '+ str(e))
        output = str(e)
        resp = jsonify(health="unhealthy")
        resp.status_code = 500
        return resp

    resp = jsonify(health="healthy")
    resp.status_code = 200
    return resp


# TODO possibly check env vars if not passed in, test for failure of this

def create_flask_app(name: str, dbconnstr: str) -> Flask: 
    app = Flask(name)
    app.config['SQLALCHEMY_DATABASE_URI'] = dbconnstr
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.db = SQLAlchemy(app)
    app.register_blueprint(healthcheck_blueprint)

    xray_recorder.configure(service='Flask Rest API')
    XRayMiddleware(app, xray_recorder)

    return app
