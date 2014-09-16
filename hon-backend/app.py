# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.restful import Api

from hon.config import Config


app = Flask(__name__)

# Configure server based on Config class
app.config.from_object(Config)

try:
    from hon.localconfig import LocalConfig
    app.config.from_object(LocalConfig)
except ImportError:
    print ' * * localconfig not found, loading from Config only.'


api = Api(app, prefix='/api')
