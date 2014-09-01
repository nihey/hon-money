# -*- coding: utf-8 -*-

from flask import request
from flask.ext.restful import fields, marshal
import psycopg2

from app import api
from hon.api.base import BaseResource
from hon.api.decorators import FinalResource
from hon.api.fields import DateTimeInt
from hon.utils import json_response, get_logged_user
from hon.models.user import Account, Transaction
from hon.database.runtime import get_default_store


@FinalResource
class AccountResource(BaseResource):

    properties = {
        'id': fields.Integer,
        'name': fields.String,
        'creation_date': DateTimeInt,
        'user_id': fields.Integer,
        'sum': fields.Float,
    }

    table = Account

    filters = {
        'user_id': Account.user_id,
    }

    def post(self):
        user = get_logged_user()
        if not user:
            return json_response(403, {'error': 'User not authenticated'})
        name = request.form['name']

        account = Account()
        account.name = name
        account.user = user

        store = get_default_store()
        try:
            store.add(account)
            store.commit()
        except psycopg2.IntegrityError:
            store.rollback()
            return json_response(403, {'error': 'IntegrityError'})
        return marshal(account, self.properties)

    #
    # BaseResource Hooks
    #

    def filter(self, data):
        user = get_logged_user()
        return [d for d in data if d.authenticate(user)]


@FinalResource
class TransactionResource(BaseResource):

    properties = {
        'id': fields.Integer,
        'name': fields.String,
        'value': fields.Float,
        'transaction_date': DateTimeInt,
        'creation_date': DateTimeInt,
        'account_id': fields.Integer,
    }

    table = Transaction

    filters = {
        'account_id': Transaction.account_id,
    }

    def post(self):
        user = get_logged_user()
        if not user:
            return json_response(403, {'error': 'User not authenticated'})
        name = request.form['name']
        value = request.form['value']
        date = request.form['date']
        account_id = request.form['account_id']

        store = get_default_store()
        account = Account.find(store, account_id)
        if not account:
            return json_response(403, {'error': 'Account does not exists'})
        if not account.authenticate(user):
            return json_response(403, {'error': 'Account not authenticated'})

        transaction = Transaction()
        transaction.name = name
        transaction.value = value
        transaction.transaction_date = date
        transaction.account = account

        try:
            store.add(transaction)
            store.commit()
        except psycopg2.IntegrityError:
            store.rollback()
            return json_response(403, {'error': 'IntegrityError'})
        return marshal(transaction, self.properties)

    #
    # BaseResource Hooks
    #

    def filter(self, data):
        # FIXME There should be a better way to do this
        user = get_logged_user()
        return [d for d in data if d.authenticate(user)]


def register_account_resource():
    api.add_resource(AccountResource, '/accounts', endpoint='accounts')
    api.add_resource(TransactionResource, '/transactions',
                     endpoint='transactions')
