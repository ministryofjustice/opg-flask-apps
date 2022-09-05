from flask import Blueprint, render_template
from flask import jsonify
from flask import current_app
import logging

home_blueprint = Blueprint("home_blueprint", __name__)


@home_blueprint.route("/")
def home():
    return render_template("index.html")
