# encoding=utf8

import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import requests

def fetch(pid):
    resp = requests.get('http://www.baidu.com')
    result = resp.text
    datetime = resp.text[:10]

    print 'Process %s: %s' % (pid, datetime)
    return result

def synchronous():
    for i in xrange(1, 10):
        fetch(i)

def asychronous():
    threads = []
    for i in xrange(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print 'Synchronous:'
synchronous()

print 'Asynchronous:'
asychronous()