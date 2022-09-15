from pathlib import Path
from flask import Flask, render_template
from flask_assets import Bundle, Environment
from flask_compress import Compress
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from govuk_frontend_wtf.main import WTFormsHelpers
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader, FileSystemLoader
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from .home_blueprint import home_blueprint
from .healthcheck_blueprint import healthcheck_blueprint


def create_flask_app(name: str, force_https=True, loaders=[]) -> Flask:
    """Create a new flask app

    Parameters:
    force_https (boolean): This tells Talisman to force redirect to https, can be overridden here to turn it off
    loaders(List): List of loaders to tell Jinja where to look for templates. This allows extra loaders to be added by calling code

    Returns: A Flask app

    """
    app = Flask(__name__, static_url_path="/assets")
    xray_recorder.configure(service=f"{name} Flask Front API")
    XRayMiddleware(app, xray_recorder)

    loaders.extend(
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
    app.jinja_loader = ChoiceLoader(loaders)

    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    csp = {"default-src": "'self'"}

    Compress(app)
    Talisman(
        app,
        content_security_policy=csp,
        strict_transport_security_max_age=3600,
        force_https=force_https,
    )
    csrf = CSRFProtect(app)

    # set up WTForms and related assets
    WTFormsHelpers(app)

    assets = Environment(app)
    js = Bundle("src/js/*.js", filters="jsmin", output="dist/js/custom-%(version)s.js")
    assets.register("js", js)

    app.register_blueprint(home_blueprint)
    app.register_blueprint(healthcheck_blueprint)

    app.register_error_handler(404, not_found)
    app.register_error_handler(500, internal_server_error)

    return app


def not_found(error):
    return render_template("opgflaskfront/404.html"), 404


def internal_server_error(error):
    return render_template("opgflaskfront/500.html"), 500
