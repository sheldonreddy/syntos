#!/usr/bin/env python3
import speech_recognition as sr
import flask
import pyttsx3
from flask import request, jsonify
from time import sleep

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=["GET", "POST"])
def playsound():
    return '''<!DOCTYPE html>                                       <html>                                                        <link rel="stylesheet" href="static/style.css">                                                     <body>                                                                                                                                                            <form action="/" method="POST" style="border:1px
solid #ccc">                                            <div class="container">                                 <h1>Play sound</h1>                                        <hr>                                                                                                        <input id="text" type="text" placeholder="Text to play" name="text" required>                                                                                     <button type="submit" class="signupbtn">Play</button>                                                       </div>                                              </div>                                              </form>                                               
</body>'''


# curl "http://localhost:5000/api/v1/test?param=hello"
@app.route('/api/v1/test', methods=['GET'])
def api_test():
    query_parameters = request.args
    value = query_parameters.get('param')
    return jsonify(value)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# curl "http://localhost:5000/api/v1/tts?text=hello+you"
@app.route('/api/v1/tts', methods=['GET'])
def api_tts():
    query_parameters = request.args
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',
                       'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0')
    texttospeak = query_parameters.get('text')
    engine.say(texttospeak)
    engine.runAndWait()
    return jsonify("Text To Speech Request Completed")


# curl "http://localhost:5000/api/v1/stt?text=hello+you"
@app.route('/api/v1/stt', methods=['GET'])
def api_sst():
    query_parameters = request.args
    texttospeak = query_parameters.get('text')

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice',
                       'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0')
    engine.say("Speech to text engine is now listening")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        sphinxout = r.recognize_sphinx(audio)
        engine.setProperty('voice',
                           'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0')
        engine.say(sphinxout)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    return jsonify("Speech Request Completed")


# curl "http://localhost:5000/api/v1/sttful?text=hello+you"
@app.route('/api/v1/sttfull', methods=['GET'])
def api_sstfull():
    query_parameters = request.args
    texttospeak = query_parameters.get('text')

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice',
                       'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0')
    engine.say("Speech to text engine is now listening")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        sphinxout = r.recognize_sphinx(audio)
        engine.setProperty('voice',
                           'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0')
        engine.say(sphinxout)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

    return jsonify("Text To Speech Request Completed")

app.run()
