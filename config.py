import os

class Config(object):
    SECRET_KEY = os.environ.get('SECTRET KEY') or 'you will never guess'