FROM python:3.10.0

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt



RUN apt update && \
  apt-get install -y libsndfile1-dev ffmpeg lilypond libsox-fmt-all


COPY .. .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
