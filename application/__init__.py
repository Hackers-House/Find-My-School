from flask import Flask
#this is a special variable named to indentify the current application that is being rendered or passed to flask
app=Flask(__name__)

from application import routes