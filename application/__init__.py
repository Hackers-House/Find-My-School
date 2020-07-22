from flask import Flask
from config import Config
import pyodbc
#this is a special variable named to indentify the current application that is being rendered or passed to flask
app=Flask(__name__)
app.config.from_object(Config)
from application import routes