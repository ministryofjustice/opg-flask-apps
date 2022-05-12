from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import logging

from app import app

@app.route("/healthcheck")
def healthcheck():
    try:
        app.db.session.execute('SELECT 1')
    except Exception as e:
        logging.error('Failed to connect: '+ str(e))
        output = str(e)
        resp = jsonify(health="unhealthy")
        resp.status_code = 500
        return resp

    resp = jsonify(health="healthy")
    resp.status_code = 200
    return resp
