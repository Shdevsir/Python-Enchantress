FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python python3-pip
RUN pip3 install flask
COPY app.py /opt/test_app/
ENTRYPOINT FLASK_APP=/opt/test_app/app.py flask run --host=0.0.0.0 --port=8080
