# -*- coding: utf-8 -*-

from time import mktime

from flask.ext.restful import fields


class DateTimeInt(fields.Raw):
    def format(self, value):
        """ Converte o valor datetime para uma representação inteira.
        """
        time = mktime(value.timetuple()) * 1000
        return int(time)
