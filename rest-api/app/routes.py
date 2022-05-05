from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from app import app

@app.route("/healthcheck")
def healthcheck():
    resp = jsonify(health="healthy")
    resp.status_code = 200
    return resp
