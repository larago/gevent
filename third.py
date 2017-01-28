# encoding=utf8

import gevent
import random

def task(pid):
    '''Some non-deterministic task'''
    gevent.sleep(random.randint(0,2)*0.001)
    print 'Task %s done' % pid

def synchronous():
    for i in xrange(1, 10):
        task(i)

def asynchronus():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)

print 'Synchronous:'
synchronous()

print 'Asynchronous:'
asynchronus()