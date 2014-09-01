# -*- coding: utf-8 -*-

import json

from flask import make_response, session

from hon.database.runtime import get_default_store
from hon.models.user import User


class Settable(object):

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)


def json_response(status_code, json_dict):
    response = make_response(json.dumps(json_dict))
    response.status_code = status_code
    response.content_type = 'application/json'
    return response


def is_logged_in():
    return 'username' in session and 'id' in session


def get_logged_user():
    store = get_default_store()
    return User.find(store, session.get('id', None))
