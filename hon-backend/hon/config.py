# -*- coding: utf-8 -*-


class Config(object):
    DEBUG = True

    RDBMS = 'postgres'
    DB_NAME = 'hon'
    DB_USER = 'hon'
    DB_PASS = ''
    DB_HOST = 'localhost'

    ALLOWED_DOMAIN = 'http://localhost:4200'

    SECRET_KEY = (')\xda\xa6e\xd1\x848}\x9d}\x04\xd3sy4j\x10\xbfh0\xca\x8fH%'
                  '\xe9\xb4\xbb\xbb\xed1\xdc;\xaa>x')
