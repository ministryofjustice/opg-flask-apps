from flask import Flask
from opgflaskapi import create_flask_app
import sqlite3
db = sqlite3.connect(':memory:')

def test_create_flask_app_with_db():
    api = create_flask_app("bob", ':memory:')
    assert isinstance(api, Flask)

def test_create_flask_app_without_db():
    api = create_flask_app("bob", None)
    assert isinstance(api, Flask)

    # TODO need to call healthcheck route
