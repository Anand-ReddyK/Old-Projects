from flask import Flask, render_template, request
import tasks

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home_page():
    all_tasks = []
    if request.method == "POST":
        task = request.form.get("task")
        num = request.form.get("number")

        all_tasks = tasks.add_task(task, int(num))

    return render_template("index.html", all_tasks=all_tasks)




if __name__ == "__main__":
    app.run(debug=True, threaded=True)