#All routes will be listed here
from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {"username":"Fabio"}
    title = "Home"
    return render_template("index.html", title=title, user=user)