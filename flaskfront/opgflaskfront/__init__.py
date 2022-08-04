from flask import Flask, render_template
from flask_assets import Bundle, Environment
from flask_compress import Compress
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from govuk_frontend_wtf.main import WTFormsHelpers
from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware


def create_flask_app(name: str) -> Flask:

    app = Flask(__name__, static_url_path="/assets")
    xray_recorder.configure(service=f"{name} Flask Front API")
    XRayMiddleware(app, xray_recorder)

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
    Talisman(app, content_security_policy=csp, strict_transport_security_max_age=3600)
    csrf = CSRFProtect(app)

    # set up WTForms and related assets
    WTFormsHelpers(app)

    assets = Environment(app)
    js = Bundle("src/js/*.js", filters="jsmin", output="dist/js/custom-%(version)s.js")
    assets.register("js", js)

    # TODO may want to healtcheck  as blueprint soon
    # app.register_blueprint(healthcheck_blueprint)

    app.register_error_handler(404, not_found)
    app.register_error_handler(500, internal_server_error)

    app.add_url_rule("/", view_func=index_page)
    app.add_url_rule("/completed-feedback", view_func=feedback)
    app.add_url_rule("/flask-accessibility", view_func=accessibility)
    return app


def not_found():
    return render_template("404.html"), 404


def internal_server_error():
    return render_template("500.html"), 500


def index_page():
    return render_template("index.html")


def feedback():
    return render_template("feedback.html")


def accessibility():
    return render_template("accessibility.html")
