FROM fhq9543/docker-py36_alpline_mysqlclient

COPY . /project/operation_log

WORKDIR /project/operation_log

RUN pip install -r requirements.txt

CMD ["uwsgi", "/project/operation_log/operation_log/wsgi/uwsgi.ini"]
