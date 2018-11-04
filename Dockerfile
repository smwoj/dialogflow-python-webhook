FROM python:3.6

COPY src/requirements.txt /
RUN apt-get install libcurl4-openssl-dev
RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE 8080

COPY src/ /repo/
WORKDIR /repo

CMD python main.py demo
