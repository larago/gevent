# encoding=utf8

import socket
print socket.socket

print 'after monkey patch'
from gevent import monkey
monkey.patch_socket()
print socket.socket

import select
print select.select
monkey.patch_select()
print select.select

