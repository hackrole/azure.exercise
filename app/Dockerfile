FROM python:3.7.4-slim-stretch

RUN mkdir /app
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["gunicorn", "web:app"]
