from flask import Flask, jsonify

from app import app

@app.route("/healthcheck")
def healthcheck():
    resp = jsonify(health="healthy")
    resp.status_code = 200
    return resp
