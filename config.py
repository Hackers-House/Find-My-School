import os
class Config(object):
    #its a key used as a signature key used to make sure the content sent isnt intercepted
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"