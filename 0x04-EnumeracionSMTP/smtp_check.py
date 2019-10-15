#!/usr/bin/python3
import socket
import sys

target = sys.argv[1]
command = sys.argv[2]

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = connect((target, 25))
    banner = sock.rev(1024)
    print (banner)

    if '220' in banner:
        with open('users.txt', 'r') as f:
            for user in f:
                sock.send(command + ' ' + user)
                result = sock.recv(1024)

                if '252' in str(result) or '250' in str(result):
                    print('Valid user: {}'.format(user))
        f.close()
    sock.close()
except socket.timeout:
    print('Timeout for: {}'.format(target))
except socket.error:
    print('Timeout for: {}'.format(target))
