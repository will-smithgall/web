import os
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/schedule")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/gen-eds")
def gen_ed():
    return render_template("gen_ed.html")

@app.route("/major-requirements")
def major():
    return render_template("major.html")

@app.route("/additional-physics")
def phys():
    return render_template("physics.html")

if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG")=="true")