import os
from opgflaskapi import create_flask_app

postgresUrl = 'postgresql://{}:{}@{}/{}'.format(
        os.getenv('POSTGRES_USERNAME') ,
        os.getenv('POSTGRES_PASSWORD') ,
        os.getenv('POSTGRES_HOSTNAME') ,
        os.getenv('POSTGRES_NAME'))

api = create_flask_app("bob", postgresUrl)
