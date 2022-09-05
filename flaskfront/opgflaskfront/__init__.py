from flask import Flask, render_template
from flask_assets import Bundle, Environment
from flask_compress import Compress
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from govuk_frontend_wtf.main import WTFormsHelpers
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from .home_blueprint import home_blueprint

# from .feedbackfront_blueprint import feedbackfront_blueprint


def create_flask_app(name: str) -> Flask:

    app = Flask(__name__, static_url_path="/assets")
    #    xray_recorder.configure(service=f"{name} Flask Front API")
    #    XRayMiddleware(app, xray_recorder)

    app.jinja_loader = ChoiceLoader(
        [
            PackageLoader("opgflaskfront"),
            PrefixLoader(
                {
                    "govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja"),
                    "govuk_frontend_wtf": PackageLoader("govuk_frontend_wtf"),
                }
            ),
        ]
    )

    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    csp = {"default-src": "'self'"}

    Compress(app)
    # Talisman(app, content_security_policy=csp, strict_transport_security_max_age=3600)
    csrf = CSRFProtect(app)

    # set up WTForms and related assets
    WTFormsHelpers(app)

    assets = Environment(app)
    js = Bundle("src/js/*.js", filters="jsmin", output="dist/js/custom-%(version)s.js")
    assets.register("js", js)

    app.register_blueprint(home_blueprint)
    # app.register_blueprint(feedbackfront_blueprint)

    app.register_error_handler(404, not_found)
    app.register_error_handler(500, internal_server_error)

    return app


def not_found(error):
    return render_template("404.html"), 404


def internal_server_error(error):
    return render_template("500.html"), 500
