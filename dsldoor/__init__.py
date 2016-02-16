import time
import zmq
import sys
import os

__all__ = ['door']


SOCK_PATH = 'tcp://127.0.0.1:9000'


def create_server_socket(ctx=None, sock_path=None, socket_type=zmq.SUB):
    ctx = ctx or zmq.Context()
    socket = ctx.socket(socket_type)
    socket.bind('{sock_path}'.format(sock_path=sock_path))

    return ctx, socket


def create_client_socket(ctx=None, sock_path=None, socket_type=zmq.PUB):
    ctx = ctx or zmq.Context()
    socket = ctx.socket(socket_type)
    socket.connect('{sock_path}'.format(sock_path=sock_path))
    return ctx, socket


def _wrap_send(command):
    _, socket = create_client_socket(sock_path=SOCK_PATH)
    time.sleep(0.1)
    socket.send(command)


class door(object):

    @staticmethod
    def open():
        _wrap_send(b'OPEN')

    @staticmethod
    def close():
        _wrap_send(b'CLOSE')
