from flask import Flask
from opgflaskapi import create_flask_app
import sqlite3
db = sqlite3.connect("file::memory:?cache=shared", uri=True)

def test_create_flask_app_with_db():
    api = create_flask_app("bob", 'sqlite:///:memory:')
    assert isinstance(api, Flask)

    response = api.test_client().get("/healthcheck")
    assert response.status_code == 200

def test_create_flask_app_without_db():
    api = create_flask_app("bob", None)
    assert isinstance(api, Flask)

    response = api.test_client().get("/healthcheck")
    assert response.status_code == 200
