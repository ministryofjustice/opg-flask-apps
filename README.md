# opg-flask-apps
Development repository: Managed by opg-org-infra &amp; Terraform

opg-flask-apps provides easily extendable base [Flask](https://flask.palletsprojects.com/en/2.1.x/) libraries, configured in a specific way for use at OPG. There is currently just an api library. A forms library using Jinja templates, is to follow shortly. The api library includes database connections (postgres supported so far), basic healthcheck, AWS xray, and will soon include authentication. The intended use is to have endpoints plugged in. (See [opg feedback repo](https://github.com/ministryofjustice/opg-feedback) for an example). There is a demo folder with an example of how to use this library within docker

## Installation
 
### Clone repo

Download the repo via:

```bash
git clone https://github.com/ministryofjustice/opg-flask-apps.git
cd opg-flask-apps
```

### Install Python libray

Then, within a docker container or a virtualenv , do
```bash
cd flaskapi
pip install -e .
```

### Use library within Python program
Please see [opg feedback repo](https://github.com/ministryofjustice/opg-feedback) for an example of how to do this.
