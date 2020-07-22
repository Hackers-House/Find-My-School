from flask import render_template,redirect,request,make_response
from application import app
from .UserDAC import GetConnection,GetTable
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

@app.route("/register")
def register():
    return render_template('register.html',register=True)

#@app.route("/user")
#def user():
#    User(UserId=1,username="anush",email="anush.venkatakrishna@gmail.com",Github_Url="",linkdln_Url="",Technologies="python ,c").save()
 #   User(UserId=2,username="anushk",email="anush@gmail.com",Github_Url="xc",linkdln_Url="xx",Technologies="python ,c").save()
    
@app.route('/test')
def test():
    data=GetTable()
    data=data[0][2]
    return render_template('test.html', data=data)
