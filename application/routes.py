from flask import render_template,redirect
from application import app

#create sime route
@app.route('/')
def redir():
    return redirect('/index')
@app.route("/index")
@app.route("/home")
def index():
    return render_template('index.html',login=False)

@app.route("/login")
def login():
    return render_template('login.html',login=False)

@app.route("/events")
def events():
    return render_template('events.html',login=False)

@app.route("/register")
def register():
    return render_template('register.html',login=False)
