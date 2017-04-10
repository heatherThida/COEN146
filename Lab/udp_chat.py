# Lab5
# COEN 146L (Wed) Thida Aung 
# TA. Arman Elahi
# This lab is to implement a partial TCP implementation by keep transferring
# messages until we get a FIN packet. To mock TCP, we identify each packet and
# ensure FIFO ordering as well as ensuring the correctness of the message
#


import re
import selectors
import socket
import sys

peers = {}
selector = selectors.DefaultSelector()
linux_host = re.compile(r'(linux60\d{3})')
PORT = 6969

def setup_chat_socket():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.bind((socket.gethostname(), PORT))
    sock.setblocking(False)
    
    selector.register(sock, selectors.EVENT_READ, print_message)
    selector.register(sys.stdin, selectors.EVENT_READ, send_message)

    try:
        while True:
            events = selector.select(timeout=0.1)
            for key, mask in events:
                handler = key.data
                handler(key.fileobj)
    except ValueError:
        print ('No more peers, someone asked me to quit. \nExiting')

def print_message (sock):
    data, address = sock.recvfrom(1024)
    host = address[0]
    message = data.decode('ascii', 'ignore')

    if message.startswith('::'):
        peers[host] = data[2:]
        print ('User {} at IP({}) connected'.format(message[2:], host))
        return 

    if message.startswith(';;'):
        message = message[2:]

    if host in peers:
        print ('{}: {}'.format(peers[host], message))
    else:
        print ('{}: {}'.format(host, message))

    if 'quit' in message or 'QUIT' in message:
        if host in peers:
            del peers[host]
        if len(peers) == 0:
            selector.close()
            sock.close()
    
def send_message(f):
    message = input()
    user = message.split()[0]

    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # no match is found, this is broadcast to all peers
    matches = linux_host.match(user)
    if not matches:
        for host in peers:
            sock.sendto(message.encode('ascii'), (host, PORT))
    else:
        host = matches.group(1)
        message = message[0:matches.start(1)] + message[(matches.end(1)+1):]
        address = socket.getaddrinfo(host, PORT, 0, socket.SOCK_DGRAM, 0,
                    socket.AI_ADDRCONFIG | socket.AI_V4MAPPED)[0][4]
        peers[address[0]] = host
        sock.sendto(message.encode('ascii'), address)

if  __name__ == '__main__':
    print ('Just start typing messages to send. If you want to send to a specific machine, you can use that linux hostnumber. If they have sent you a message already with their username, you can refer to them by username.\n---')
    setup_chat_socket()
