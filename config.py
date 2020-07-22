import os
class Config(object):
    #its a key used as a signature key used to make sure the content sent isnt intercepted
    SECRET_KY = os.environ.get('SECRET_KEY') or "secret_string"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False