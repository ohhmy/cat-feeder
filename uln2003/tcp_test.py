#! /usr/bin/env python2

import socket
import threading
import tcp_stepper
import time
import re

def tcplink(sock, addr):
    print 'Accept new connection form %s:%s...' % addr
    sock.send('welcome!\n')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        print data

        try:
            count = int(re.sub('\D','',data))
            sock.send('Hello,%s!\n' % data)
            tcp_stepper.main(count)
        except ValueError:
            sock.send('wrong! exit.\n')
            break
        else:
            break
    sock.close()
    print 'Connectioin from %s:%s closed' % addr



s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('192.168.1.129',9999))
s.listen(5)
print 'Waiting for connection...'

while True:
    sock, addr =s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


