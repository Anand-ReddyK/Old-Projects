from datetime import date
from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    trans = ''
    if request.method == 'POST':
        
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)
        
        if file:
            recog = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data1 = recog.record(source)
            text = recog.recognize_google(data1, key=None)
            trans += text
        
    return render_template('index.html', tutu=trans)

@app.route('/com')
def comp():
    print('yaaaa')
    return render_template('mes.html')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
# 0190fee5