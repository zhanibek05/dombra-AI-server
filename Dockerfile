FROM python:3.8.0

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN pip install -r pysndfile

RUN apt update && \
  apt-get install -y libsndfile1-dev ffmpeg lilypond

COPY .. .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
