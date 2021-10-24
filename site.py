import re
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/gen-eds")
def gen_ed():
    return render_template("gen_ed.html")

@app.route("/major-requirements")
def major():
    return render_template("major.html")

if __name__ == "__main__":
    app.run(debug=True)