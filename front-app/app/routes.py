from flask import render_template
from werkzeug.exceptions import NotFound

from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server(error):
    return render_template("500.html"), 500

@app.route("/healthcheck")
def healthcheck():
    return
