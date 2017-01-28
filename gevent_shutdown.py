# encoding=utf8

import gevent
import signal

def run_forever():
    gevent.sleep(2)

print dir(gevent)

if __name__ == '__main__':
    gevent.signal(signal.SIGQUIT, gevent.killall)
    thread = gevent.spawn(run_forever)
    thread.join()