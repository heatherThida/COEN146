# -*- coding: utf-8 -*-
# Thida Aung COEN 146L Lab5
# Stop and Go Packet Transfer
# The server should always first receive a packet and then send another packet back.
# The server should use the exact same struct as the client, expecting Packet structure.
#

import socket
import sys
import json


MAX_NUM_OF_BYTES = 10000000
port = 6932
localhost = 'localhost'

def server(port):
    """Server program modeling TCP interaction with clients"""
    """Listen and receive a file, binding to the given port."""
    # Create a socket object specifying arguments to have UDP transport
    # family-IPv4, type-UDP,gethostn protocol- default = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    
    # Bind the socket object to your localhost and port
    sock.bind((localhost, port))

    print ('Socket Initialized')

    while True:
       packet = {
           "message": "",
           "type": "",
           "checksum": 0,
           "seq": 0
       }

       # Receive the message, decode the message and load them as json objects into data 
       message, address = sock.recvfrom(MAX_NUM_OF_BYTES)	
       message= message.decode('ascii', 'ignore')	
       data = json.loads(message)
       # Check if the type is FIN, print then quit.
       if data["type"].startswith("FIN"):
            #packet["type"]="FIN"
            #packet["message"]=""
            #packet["seq"]=0	
            print ("Final message!")
            break

       else:
           
            #check the checksum, create the packet
            if sum(ord(char) for char in data["message"]) == data["checksum"]:
                    #prepare the packet
                    packet["type"]= "ACK"
                    packet["seq"]= data["seq"]+1
                    print (data["message"])
            else:
                    
                    #resend the packet
                    packet["type"]= "ACK"
                    packet["seq"]=data["seq"]
                    print(data["message"])
            
            #send to the client
            data =json.dumps(packet)
            sock.sendto(data.encode('ascii','ignore'), address)

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


