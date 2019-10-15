#!/usr/bin/python3
import dns.name

n = dns.name.from_text('www.google.com')
n1 = dns.name.from_text('google.com')
# if n1 is domian of n
print(n.is_subdomain(n1))
"""
>>> True

"""
print(n.relativize(n1))
"""
>>> www

"""
print(n.labels)
"""
>>> ('www', 'google', 'com', '')

"""
print(n1.labels)
"""
>>> ('google', 'com', '')

"""


