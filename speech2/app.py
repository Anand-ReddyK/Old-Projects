from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)


@app.route('/', methods=['GET', "POST"])
def index():
    text = "hrllocjthxhh"
    if request.method == "POST":
        print("Form data received")

        if "file" not in request.files:
            return redirect(request.url)
        
        file = request.files["file"]

        if file.filename == "":
            return redirect(request.url)
        
        if file:
            recognizer = sr.Recognizer()
            audiofile = sr.AudioFile(file)
            with audiofile as source:
                data = recognizer.record(source)
            text = recognizer.recognize_google(data, key=None)
            
    return render_template("index.html", text = text)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)