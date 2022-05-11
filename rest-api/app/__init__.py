import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)

postgresUrl = 'postgresql://{}:{}@{}/{}'.format(
        os.getenv('POSTGRES_USERNAME') , 
        os.getenv('POSTGRES_PASSWORD') , 
        os.getenv('POSTGRES_HOSTNAME') , 
        os.getenv('POSTGRES_NAME'))
app.config['SQLALCHEMY_DATABASE_URI'] = postgresUrl
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.db = SQLAlchemy(app)

xray_recorder.configure(service='Flask Rest API')
XRayMiddleware(app, xray_recorder)

from app import routes
