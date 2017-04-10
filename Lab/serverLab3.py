# -*- coding: utf-8 -*-
# Thida Aung COEN 146L Lab3
#
# Copying Data Via UDP Sockets datagrams using socket program template.
# This is Server that open and read a file we passed in from Client and write it line by line.
# Upon receiving filename, address passed from recvfrom() method,we open it to start writing.
# Messages were encoded from client side upon sending and server decode all the data as ascii
# upon receival so we can properly write out to the file. Then we give it a new file name and
# copied those data and write in that file until we see “” string. 



import socket
import sys

localhost = 'localhost'
MAX_NUMBER_OF_BYTES = 100000000
port = 6932


def server(port):        
    """Listen and receive a file, binding to the given port."""
    # Create a socket object specifying arguments to have UDP transport
    # family, UDP, protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )

    # Bind the socket object to your localhost and port
    sock.bind((localhost, port))
    print ('Socket Initialized')
    # Receive a filename and open a file
    file_name, address = sock.recvfrom(MAX_NUMBER_OF_BYTES)

    with open(file_name, 'w') as f:
       while True: 
         # Poll for all the data that should go into the file
         data,address = sock.recvfrom(MAX_NUMBER_OF_BYTES)
         if data:
             #calling this method on a string to decode data into ascii format
             f.write(data.decode('ascii', 'ignore'))
         else:
            break
    # Close the socket
    sock.close()

if __name__ == '__main__':
    if len (sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            server (port)
        except ValueError:
            raise
    else:
            print ('Usage: python3 server.py port')
