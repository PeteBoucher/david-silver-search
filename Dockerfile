FROM python:3.7-stretch

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY features /app/features

CMD [ "behave" ]