#encoding=utf8

import gevent
from gevent import Timeout

seconds = 2

timeout = Timeout(seconds)
timeout.start()

def wait():
    gevent.sleep(1)

try:
    gevent.spawn(wait).join()
except Timeout:
    print 'could not complete'