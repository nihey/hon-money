# -*- coding: utf-8 -*-

from datetime import datetime
from hashlib import sha512

from storm.expr import And
from storm.properties import DateTime, Decimal, Int, Unicode
from storm.references import Reference, ReferenceSet

from hon.database.runtime import get_default_store
from hon.models.base import BaseModel


class User(BaseModel):

    __storm_table__ = "hon_user"

    # Authentication data
    username = Unicode()
    password = Unicode()

    accounts = ReferenceSet('User.id', '')

    # Misc data
    creation_date = DateTime()

    def __init__(self):
        self.creation_date = datetime.now()

    #
    # Static API
    #

    @staticmethod
    def hash(password):
        return unicode(sha512(password).hexdigest())

    @classmethod
    def authenticate(cls, store, username, password):
        query = And(cls.username == username,
                    cls.password == cls.hash(password))
        return store.find(cls, query).one()

    #
    # Public API
    #

    def set_password(self, password):
        self.password = self.hash(password)


class Account(BaseModel):

    __storm_table__ = "hon_account"

    name = Unicode()

    # Account user
    user_id = Int()
    user = Reference(user_id, 'User.id')

    # Misc data
    creation_date = DateTime()

    def __init__(self):
        self.creation_date = datetime.now()

    #
    # Implicit Properties
    #

    @property
    def sum(self):
        store = get_default_store()
        transactions = store.find(Transaction, account_id=self.id)
        return sum(transactions)

    #
    # Public API
    #

    def authenticate(self, user):
        return user.id == self.user_id


class Transaction(BaseModel):

    __storm_table__ = "hon_transaction"

    # Transaction required data
    name = Unicode()
    value = Decimal()
    transaction_date = DateTime()

    description = Unicode()

    # Account user
    account_id = Int()
    account = Reference(account_id, 'Account.id')

    # Misc data
    creation_date = DateTime()

    def __init__(self):
        self.creation_date = datetime.now()

    #
    # Public API
    #

    def authenticate(self, user):
        return user.id == self.account.user_id
