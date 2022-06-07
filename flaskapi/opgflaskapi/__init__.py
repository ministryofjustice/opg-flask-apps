from flask import Flask 

# TODO pass in postgres creds,  name becomes a config obj passed in after extracting from env,  with db type
# exceptions if not passed in, tests of this   possibly use Config library
# possibly check env vars if not passed in
def create_flask_app(name: str) -> Flask: 
    return Flask(name)
