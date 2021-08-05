FROM python:3.7.11-alpine3.14

WORKDIR /opt
COPY . /opt
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "main.py"]
