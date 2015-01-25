import json

from flask import (Flask, render_template, redirect, url_for, request, make_response)
# from flask_bootstrap import Bootstrap
# from options import DEFAULTS

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")

 
# @app.route('/builder')
# def builder():
#   return render_template(
#     "builder.html",
#     saves=get_saved_data(),
#     options=DEFAULTS
#   )


# @app.route("/save", methods=["POST"])
# def save():
#   response = make_response(redirect(url_for("builder")))
#   data = get_saved_data()
#   data.update(dict(request.form.items()))
#   response.set_cookie("character", json.dumps(data))
#   return response

app.run(debug=True)
