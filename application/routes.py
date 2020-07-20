from flask import render_template,redirect
from application import app

#create sime route
@app.route('/')
def redir():
    return redirect('/index')
@app.route("/index")
def index():
    return render_template('index.html')
