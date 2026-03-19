from flask import Flask, render_template, request
from functions import safe_get, safe_get_ranArt
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
        curCon = safe_get(location=request.form["user_location"])
        artwork = safe_get_ranArt(con=curCon)
        return render_template("results.html", curCon=curCon, artwork=artwork)
    else:
        return "Wrong HTTP method", 400
