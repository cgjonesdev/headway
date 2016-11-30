#!/usr/bin/env python

'''
Provides a set of utility objects for the rest of the code base.
'''

from api import HOST, PORT
from socket import socket, AF_INET, SOCK_STREAM

def is_open_socket():
    sock = socket(AF_INET, SOCK_STREAM)
    return sock.connect_ex((HOST, int(PORT[1:])))
