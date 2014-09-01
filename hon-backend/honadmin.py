# -*- coding: utf-8 -*-

import sys

import IPython
from storm.tracer import debug

from hon.database.runtime import *
from hon.models.user import *


if __name__ == '__main__':
    store = get_default_store()

    if len(sys.argv) < 2:
        print 'Usage: python honadmin.py [OPTIONS]'
        print ''
        print "'OPTIONS' is one of:"
        print ''
        print 'create_user <name>                          New user'
        print '--sql                                       Show sql commands'
        print '--console                                   Enter console mode'
        print ''


    if '--sql' in sys.argv:
        debug(True, stream=sys.stdout)

    if 'create_user' in sys.argv:
        option_index = sys.argv.index('create_user')

        user = User()
        user.username = unicode(sys.argv[option_index+1])
        user.set_password(unicode(raw_input('password: ')))
        store.add(user)
        store.commit()

    if '--console' in sys.argv:
        IPython.embed()
