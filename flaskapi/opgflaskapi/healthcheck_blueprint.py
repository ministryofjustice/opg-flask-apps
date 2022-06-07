from flask import Blueprint

healthcheck_blueprint = Blueprint('healthcheck_blueprint', __name__)

@healthcheck_blueprint.route('/')
def index():
    return "This is a healthcheck"
