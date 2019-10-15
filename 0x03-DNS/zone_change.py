#!/usr/bin/python3
import dns.query
import dns.zone

# get IP of register IPV4 from Domain  an paste in query
try:
    z = dns.zone.from_xfr(dns.query.xfr('127.0.0.1', 'domaincom'))
except socket.error as err: # closed socket
    print("{}".format(err))
