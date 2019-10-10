#!/usr/bin/python3

import socket
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for host in range(0, 254):
    ports = open('ports.txt', 'r')
    vulbanners = open('vulbanners.txt', 'r')
    for port in ports:
        try:
            socket.connect((str(sys.argv[1] + '.' + str(host) ) , int(port)))
            print('Connecting to {}.{} in the port {}'.format(
                sys.argv[1], host, port))
            socket.settimeout(1)
            banner = socket.recv(1024)
            for vulbanner in vulbanners:
                if banner.strip() in vulbanner.strip():
                    print("We have a winner {}".format(banner))
                    print("Host: {}.{}".format(sys.argv[1], host))
                    print("Port: {}".format(port))
        except: 
            pass
