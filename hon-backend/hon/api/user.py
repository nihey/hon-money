# -*- coding: utf-8 -*-

from flask import request, session
from flask.ext.restful import fields, marshal, Resource

from app import api
from hon.api.base import BaseResource
from hon.api.decorators import FinalResource
from hon.api.fields import DateTimeInt
from hon.utils import json_response
from hon.models.user import User
from hon.database.runtime import get_default_store


@FinalResource
class UsersResource(BaseResource):

    properties = {
        'id': fields.Integer,
        'username': fields.String,
    }

    table = User

    filters = {
        'username': User.username,
    }


class LoginResource(Resource):

    properties = {
        'id': fields.Integer,
        'username': fields.String,
        'creation_date': DateTimeInt,
    }

    def get(self):
        store = get_default_store()
        user = User.find(store, session.get('id', None))
        if user:
            return marshal(user, self.properties)
        return json_response(403, {'error': 'User not authenticated'})

    def post(self):
        username = request.form['username']
        password = request.form['password']
        store = get_default_store()

        user = User.authenticate(store, username, password)
        if user:
            session['username'] = user.username
            session['id'] = user.id
            return marshal(user, self.properties)
        return json_response(403, {'error': 'Invalid username or password.'})

    def delete(self):
        session.pop('username', None)
        session.pop('id', None)
        return json_response(200, {'message': 'User has been logged out.'})


def register_user_resource():
    api.add_resource(UsersResource, '/users', endpoint='users')
    api.add_resource(LoginResource, '/login', endpoint='login')
