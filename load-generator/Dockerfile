FROM python:3.7-buster

WORKDIR /

COPY requirements.txt ./

RUN pip3 install -r /requirements.txt

COPY sim.py /sim.py

ENTRYPOINT python3 sim.py
