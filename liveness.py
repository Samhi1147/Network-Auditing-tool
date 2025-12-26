import os
import platform

import socket

def is_alive(host):
    try:
        socket.create_connection((host, 80), timeout=3)
        return True
    except:
        return False