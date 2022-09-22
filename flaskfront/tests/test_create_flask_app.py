from flask import Flask
from opgflaskfront import create_flask_app
from jinja2 import FileSystemLoader


def test_create_flask_app():
    app = create_flask_app("bob", force_https=False)
    assert isinstance(app, Flask)

    response = app.test_client().get("/")
    assert response.status_code == 200

    response = app.test_client().get("/healthcheck")
    assert response.status_code == 200


def test_create_flask_app_passing_in_loader():
    loaders = [FileSystemLoader("."), FileSystemLoader("..")]

    app = create_flask_app("bob", force_https=False, loaders=loaders)
    assert isinstance(app, Flask)

    response = app.test_client().get("/")
    assert response.status_code == 200

    response = app.test_client().get("/healthcheck")
    assert response.status_code == 200

    response = app.test_client().get("/assets/govuk-frontend-3.14.0.min.css")
    assert response.status_code == 200

    response = app.test_client().get("/assets/govuk-frontend-3.14.0.min.js")
    assert response.status_code == 200

    # ensure we get a working 404 not any breakage or a 500
    response = app.test_client().get("/does-not-exist")
    assert response.status_code == 404
