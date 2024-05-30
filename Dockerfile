FROM python:3.9.16-bullseye

WORKDIR /marketuci/
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt update; apt-get install -yy apache2

CMD ["bash","run.sh"]

EXPOSE 10000