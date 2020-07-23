from flask import render_template,redirect,request,make_response,flash,url_for
from application import app
from .UserDAC import *
from application.forms import RegisterForm
#create sime route
@app.route('/')
def redir():
    return redirect('/index')
@app.route("/index")
@app.route("/home")
def index():
    return render_template('index.html',index=True)

@app.route("/blog")
def blog():
    return render_template('blog.html',blog=True)

@app.route("/events")
def events():
    return render_template('events.html',events=True)

@app.route("/register",methods=['POST','GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        userID     = GetIndex()
        userID    += 1
        username    =form.username.data
        email       = form.email.data
        Github      =form.Github.data
        linkdln     =form.linkdln.data
        Tech        =form.Tech.data 
        SetData(userID,username,email,Github,linkdln,Tech)   
        flash("You are successfully registered!","success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Want to Mentor ? Register With Us", form=form,register=True)

#@app.route("/user")
#def user():
#    User(UserId=1,username="anush",email="anush.venkatakrishna@gmail.com",Github_Url="",linkdln_Url="",Technologies="python ,c").save()
 #   User(UserId=2,username="anushk",email="anush@gmail.com",Github_Url="xc",linkdln_Url="xx",Technologies="python ,c").save()
    
@app.route('/test')
def test():
    data=GetTable()
    data=data[0][2]
    return render_template('test.html', data=data)
