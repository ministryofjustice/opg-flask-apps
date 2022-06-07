# context should be set to dir above demo dir
FROM python:3.9-alpine

# security fix for expat
RUN apk upgrade expat

RUN apk add build-base curl

WORKDIR /app

COPY opgflaskapi /app/opgflaskapi/
COPY setup.py /app/
COPY demo/demoapi.py /app/

#RUN pip install -r requirements.txt -  TODO reinstate this with only gunicorn in it
RUN pip install gunicorn

RUN python setup.py build && python setup.py install

EXPOSE 8005
CMD ["gunicorn", "demoapi:api", "--bind", "0.0.0.0:8005", "--log-file", "-"]
