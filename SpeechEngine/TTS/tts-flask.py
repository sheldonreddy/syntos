import flask
from flask import request, jsonify
import pyttsx3

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=["GET", "POST"])
def playsound():
    engine = pyttsx3.init()
    engine.setProperty('rate', 110)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',
                       'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0')
    if request.method == 'GET':
        engine.say('Text To Speech Engine Starting Up')
        engine.say('Text To Speech Engine Running')
        engine.runAndWait()
        return '''<!DOCTYPE html>                                       <html>                                                        <link rel="stylesheet" href="static/style.css">                                                     <body>                                                                                                                                                            <form action="/" method="POST" style="border:1px
solid #ccc">                                            <div class="container">                                 <h1>Play sound</h1>                                        <hr>                                                                                                        <input id="text" type="text" placeholder="Text to play" name="text" required>                                                                                     <button type="submit" class="signupbtn">Play</button>                                                       </div>                                              </div>                                              </form>                                               
</body>'''
    text = request.values.get("text")
    engine.say(text)
    engine.runAndWait()
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


app.run()
