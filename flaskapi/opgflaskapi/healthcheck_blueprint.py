from flask import Blueprint
from flask import jsonify
from flask import current_app
import logging

healthcheck_blueprint = Blueprint("healthcheck_blueprint", __name__)


@healthcheck_blueprint.route("/healthcheck")
def healthcheck():
    # if this app has a db, check db,  if not just return healthy
    # print(dir(current_app.database))
    if hasattr(current_app, "database"):
        try:
            result = current_app.database.healthcheck()
            print(dir(result))
        except Exception as e:
            logging.error("Failed to connect: " + str(e))
            output = str(e)
            resp = jsonify(health="unhealthy")
            resp.status_code = 500
            return resp

    resp = jsonify(health="healthy")
    resp.status_code = 200
    return resp
