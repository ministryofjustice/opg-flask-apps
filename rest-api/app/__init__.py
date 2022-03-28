from flask import Flask
#from flask_compress import Compress
#from flask_talisman import Talisman
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)
xray_recorder.configure(service='Flask Rest API')
XRayMiddleware(app, xray_recorder)

#csp = {
#    "default-src": "'self'"
#}

#Compress(app)
#Talisman(app, content_security_policy=csp, strict_transport_security_max_age=3600)

from app import routes
