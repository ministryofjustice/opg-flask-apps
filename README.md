# opg-flask-apps
Development repository: Managed by opg-org-infra &amp; Terraform

opg-flask-apps provides easily extendable base [Flask](https://flask.palletsprojects.com/en/2.1.x/) libraries, configured in a specific way for use at OPG. There is currently just an api library. A forms library using Jinja templates, is to follow shortly. The api library includes database connections (postgres supported so far), basic healthcheck, AWS xray, and will soon include authentication. The intended use is to have endpoints plugged in. (See [opg feedback repo](https://github.com/ministryofjustice/opg-feedback) for an example).

## Installation

### Clone repo

Download this repo via:

```bash
git clone https://github.com/ministryofjustice/opg-flask-apps.git
cd opg-flask-apps
```

### Install the Python library

Then, within a docker container or a virtualenv , do
```bash
cd flaskapi
pip install -e .
```

### In a python program, call create_flask_app to make the Flask app

(This example uses postgres, but other DBs such as sqlite could be used)

```bash
import os
from opgflaskapi import create_flask_app

postgres_url = "postgresql://{}:{}@{}/{}".format(
    os.getenv("POSTGRES_USERNAME"),
    os.getenv("POSTGRES_PASSWORD"),
    os.getenv("POSTGRES_HOSTNAME"),
    os.getenv("POSTGRES_NAME"),
)

api = create_flask_app("feedback", postgres_url)
```

### Plug in blueprint(s) to provide api endpoint(s)

```bash
from .feedback_blueprint import feedback_blueprint
api.register_blueprint(feedback_blueprint)
```

Please see [opg feedback repo](https://github.com/ministryofjustice/opg-feedback) for an in depth example of how to do this.
