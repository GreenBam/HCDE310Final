from flask import Flask, render_template, request
from functions import safe_get, get_ran
from keys import vkey

# Create an instance of Flask
app = Flask(__name__)

# Create a view function for /
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["GET", "POST"])
def results_page():
    if request.method == "POST":
        unit=request.form["unit"]
        curCon = safe_get(location=request.form["user_location"], unit=unit)
        artwork = get_ran(con=curCon)
        if unit == "us":
            degree = "F"
        elif unit == "metric":
            degree = "C"
        else:
            degree = "K"
        return render_template("results.html", curCon=curCon, artwork=artwork, degree=degree)
    else:
        return "Wrong HTTP method", 400
