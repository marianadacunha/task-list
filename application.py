from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# Enable sessions for this flask application
Session(app)

@app.route("/")
def tasks():
    if "allTasks" not in session: 
        session["allTasks"] = []
    return render_template("tasks.html", allTasks=session["allTasks"])

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        newTask = request.form.get("task")
        session["allTasks"].append(newTask)
        return redirect("/")
        
if __name__ == "__main__":
    app.run()