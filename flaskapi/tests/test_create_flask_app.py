from flask import Flask
from opgflaskapi import create_flask_app

def test_create_flask_app():
    api = create_flask_app("bob")
    assert isinstance(api, Flask)
