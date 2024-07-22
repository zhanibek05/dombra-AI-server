FROM python:3.8.0

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN apt update && \
  apt-get install libsndfile-dev

COPY .. .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
