FROM python:3.10-alpine

LABEL "channel"="Ivan"
LABEL "creator"="Ivan"

WORKDIR ./usr/lessons

COPY . .

RUN apk update && apk upgrade && apk add bash

RUN pip3 install -r requirements.txt

CMD pytest -s -v tests/*