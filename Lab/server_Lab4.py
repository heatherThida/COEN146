# -*- coding: utf-8 -*-
# Thida Aung COEN 146L Lab4
# Open Socket and let users chat using ::username or by IP address followed by ;;message
# Save users using python dictionary and quit individual user upon seeing "QUIT or quit"
# and delete when there's no more users left and close socket

import socket
import sys


localhost = 'localhost'
MAX_NUMBER_OF_BYTES = 100000000
port = 6932
 

def server(port):       
    """Listen and receive a file, binding to the given port."""
    # Create a socket object specifying arguments to have UDP transport
    # family, UDP,.gethostn protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )

    # Bind the socket object to your localhost and port
    sock.bind((localhost, port))

    print ('Socket Initialized')
    users = {} # user has key,value
    data = ""
     
    while True:
            #print regardless users is in dic or not
            data, address = sock.recvfrom(MAX_NUMBER_OF_BYTES)
            hostname = address[0]
            data = data.decode('ascii','ignore')

            if data.startswith("::"):                                 
                 users[hostname] = data[2:]
            elif data.startswith(";;"):
                 #print(messsage)
                 message = data[2:]
                 if hostname in users:
                    name = users[hostname]
                    print(name +":"+ message)
                 else:
                    name = hostname #name IP address without putting into dictionary
                    print(hostname +":"+ message)
            else:
                continue  #throw away anything else
            
            if ("quit" in data or "QUIT" in data) and hostname in users:
                del users[hostname]
                if len(users) == 0:
                    break

    sock.close()
    sys.exit()


if __name__ == '__main__':
    if len (sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            server (port)
        except ValueError:
            raise
    else:
            print ('Usage: python3 server.py port')
