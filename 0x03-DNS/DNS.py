#!/usr/bin/python3
import dns.resolver

# buscar registros
# registro para direcciones IPV4
dnsA =  dns.resolver.query('google.com', 'A')
# registro para servidores IPV6
dnsAAAA = dns.resolver.query('google.com', 'AAAA')
# Registros Servidor de correo
dnsMX =  dns.resolver.query('google.com', 'MX')
# Registro Name Server
dnsNS =  dns.resolver.query('google.com', 'NS')
# Registros para Start of authority
dnsSOA = dns.resolver.query('google.com', 'SOA')
# Regitros informacion Textual - 
dnsTXT = dns.resolver.query('google.com', 'TXT')

for dns in dnsMX:
    print(dns)
