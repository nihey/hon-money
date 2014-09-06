# -*- coding: utf-8 -*-

from storm.properties import Unicode

from hon.models.user import Transaction


class TransactionView(Transaction):

    __storm_table__ = "hon_transaction_view"

    account_name = Unicode()
