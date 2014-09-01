# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.restful import Api

from hon.config import Config


app = Flask(__name__)

# Configura o servidor a partir do arquivo de configuração em config.py
app.config.from_object(Config)

# Registra a api com prefixo '/c/r/a' (Crewee Restful API)
api = Api(app, prefix='/api')
