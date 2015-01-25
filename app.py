import json

from flask import (Flask, render_template, redirect, url_for, request, make_response)
# from options import DEFAULTS

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/info")
def info():
 	return render_template("countryInfo.html")
 
@app.route("/cultureform")
def cultureform():
  	return render_template("cultureform.html")

@app.route("/chat")
def chat():
  return render_template("chat.html")


app.run(debug=True)
