import json
#import requests

from flask import (Flask, jsonify, render_template, redirect, url_for, request, make_response)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        users_country = request.form["users_country"]
        return redirect(url_for("info", users_country=users_country))
    else:
        return render_template("index.html")
    return render_template("index.html")
@app.route("/<users_country>", methods=["GET", "POST"])
def info(users_country):
    return render_template("countryInfo.html", users_country=users_country)
 
@app.route("/cultureform", methods=["GET", "POST"])
def cultureform():
    return render_template("cultureform.html")

@app.route("/getdata")
def getData():
    url = "https://api.parse.com/1/classes/Country/"
    theKeys = {
       "X-Parse-Application-Id": "SQjJqeSyhwjwzd0NDiO4zQAqb2SQdLoDtj2EhF3e",
       "X-Parse-REST-API-Key": "SBdjen5XouoZ0NFBeFH6Q4EwfY4tr2ZxwlnNDOw6"
     }
    getRequest = requests.get(url, headers=theKeys)
    theData = getRequest.json()
    theDataCountries = theData["results"]

    return json.dumps(theDataCountries)


@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/chinainfo")
def toChina():
    return render_template("chinaInfo.html")

app.run(debug=True)
