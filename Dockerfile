FROM robo2025/python:3.6-alpine

COPY . /project/operation_log

WORKDIR /project/operation_log

RUN pip install -r requirements.txt

CMD ["uwsgi", "/project/operation_log/operation_log/wsgi/uwsgi.ini"]
