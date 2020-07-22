FROM python
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
#RUN apt-get update && apt-get upgrade -y && apt-get install -y espeak-ng
RUN apt-get update && apt-get upgrade -y && apt-get install -y libespeak-dev && apt-get install -y pulseaudio
RUN apt-get install -y alsa-utils
COPY tts-flask.py /app
ENV FLASK_APP="tts-flask"
ENV FLASK_ENV="development"
ENV FLASK_RUN_HOST="0.0.0.0"
CMD ["flask", "run"]
