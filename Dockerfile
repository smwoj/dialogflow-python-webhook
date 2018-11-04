FROM python:3.6

COPY src/requirements.txt /

RUN whoami
RUN apt-get install libcurl4-openssl-dev

RUN pip install --no-cache-dir -r /requirements.txt
EXPOSE 8080
COPY src/ /repo/
WORKDIR /repo

CMD python main.py demo




# sudo docker run -p 8080:8080 -d --name df-app  df-app:minimal
# sudo docker build -t df-app:minimal .
# sudo docker tag df-app:minimal gcr.io/hackathon-webhooks/df-app:minimal
# sudo docker push gcr.io/hackathon-webhooks/df-app:minimal
