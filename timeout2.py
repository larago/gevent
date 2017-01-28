import gevent
from gevent import Timeout

time_to_wait = 1

class TooLong(Exception):
    pass

with Timeout(time_to_wait):
    gevent.sleep(3)