#!/usr/bin/python3

from subprocess import Popen, PIPE

for ip in range(0, 255):
    ipAdd = '192.168.1.' + str(ip)
    subprocess = Popen(
        ['/bin/ping', '-c 1', ipAdd], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    stdout, stderr = subprocess.communicate(input=None)
    if "bytes from " in str(stdout):
        print("IP {}".format(ipAdd))
