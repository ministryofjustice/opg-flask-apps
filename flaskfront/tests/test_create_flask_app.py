from flask import Flask
from opgflaskfront import create_flask_app


def test_create_flask_app():
    app = create_flask_app("bob", force_https=False)
    assert isinstance(app, Flask)

    response = app.test_client().get("/")
    assert response.status_code == 200
