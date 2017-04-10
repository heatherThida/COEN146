# -*- coding: utf-8 -*-
# Thida Aung COEN 146L Lab3

# Copying Data Via UDP Sockets datagrams using socket program template.
# The Client open the file passed in from command line and transfer it line by line
# after encoding as ascii to our Server.
# So the Server can decode all the data until it sees the empty string. 

import socket
import sys

host = 'localhost'
port = 6932



def client(host, port, file_name):        
    """ Transfer file_name to a server hopefully listening at (host, port)."""
      
     # Create a socket object with the proper socket specifications.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # Resolve the IP Address given the hostname and the port number using getaddrinfo
         add = socket.getaddrinfo(host,port)
         addr = add[0][4]
     
    except socket.gaierror: 
        # insert error handling code because we couldn't resolve host name
         print("error")
         sys.exit()
    file_name2 = "test.txt"
    # Send over a different file name than what we're reading encoded properly
    sock.sendto(file_name2.encode('ascii', 'ignore'), addr)
    

    # Open the file to transfer and start sending data using the created socket object
    # At the end, you should send a control message, just an empty string to notify the end of file
    with open(file_name, 'r') as f:
       for line in f:
            # call this method on a string to encode data into ascii format
            sock.sendto(line.encode('ascii','ignore'),addr)
            
    sock.sendto("".encode('ascii', 'ignore'),addr)
    
    # Close the socket
    sock.close()

if __name__ == '__main__':
    if len (sys.argv) > 2:
        try:
            host = sys.argv[1]
            port = int(sys.argv[2])
            file_name = sys.argv[3]
            client (host, port, file_name)
        except ValueError:
            print ('Second argument should be an integer representing port number')
    
    else:
            print ('Usage: python3 client.py host port')
