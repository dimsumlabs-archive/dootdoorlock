import time
import zmq
import sys
import os

__all__ = ['door']


SOCK_PATH = '/tmp/doord'


def create_server_socket(ctx=None, sock_path=None, socket_type=zmq.SUB):
    try:
        os.unlink(sock_path)
    except OSError:
        if os.path.exists(sock_path):
            raise

    with open(sock_path, 'a'):
        os.utime(sock_path, None)

    try:
        os.chown(sock_path, -1, 1005)
        os.chmod(sock_path, 0o770)
    except OSError:
        sys.stderr.write('Cannot set socket permissions, not running as root?')
        raise

    ctx = ctx or zmq.Context()
    socket = ctx.socket(socket_type)
    socket.bind('ipc://{sock_path}'.format(sock_path=sock_path))

    return ctx, socket


def create_client_socket(ctx=None, sock_path=None, socket_type=zmq.PUB):
    ctx = ctx or zmq.Context()
    socket = ctx.socket(socket_type)
    socket.connect('ipc://{sock_path}'.format(sock_path=sock_path))
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
