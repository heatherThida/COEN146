# -*- coding: utf-8 -*-
# Thida Aung COEN 146L Lab4
# creat users chat using username or by IP address if annonymous
# ::username ;;message format and quit when typed "QUIT" or "quit" or "quitoria"


import socket
import sys

host = 'localhost'
port = 6932



def client(host, port):        
    """ Transfer file_name to a server hopefully listening at (host, port)."""
      
     # Create a socket object with the proper socket specifications.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Resolve the IP Address given the hostname and the port number using getaddrinfo
         add = socket.getaddrinfo(host,port)
         addr = add[0][4] #host,port

    except socket.gaierror: 
        # insert error handling code because we couldn't resolve host name
         print("error")
         sys.exit()
   
    while(True):
        line = input()
        #print ("Current line is: %s" % line)
        if ("quit" not in line) and ("QUIT" not in line):
            # call this method on a string to encode data into ascii format
            sock.sendto(line.encode('ascii','ignore'),addr)
        else:
            sock.sendto(line.encode('ascii','ignore'),addr)
            sys.exit()
       
    # Close the socket
    sock.close()

if __name__ == '__main__':
    if len (sys.argv) > 2:
        try:
            host = sys.argv[1]
            port = int(sys.argv[2])
            client (host, port)
        except ValueError:
            print ('Second argument should be an integer representing port number')
    
    else:
            print ('Usage: python3 client.py host port')
