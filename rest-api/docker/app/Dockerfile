FROM python:3.9-alpine

# security fix for expat
RUN apk upgrade expat

RUN apk add build-base curl
WORKDIR /restapi

COPY rest-api .
RUN pip install -r requirements.txt

EXPOSE 8005
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8005", "--log-file", "-"]
