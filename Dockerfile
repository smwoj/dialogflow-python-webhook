FROM python:3.6

COPY requirements.txt /

RUN whoami
RUN apt-get install libcurl4-openssl-dev

RUN pip install --no-cache-dir -r /requirements.txt

COPY * /repo/
WORKDIR /repo

CMD python main.py demo

