# -*- coding: utf-8 -*-
# Thida Aung COEN 146L Lab5
# Stop and Go Packet Transfer
# The client will send over a Python dictionary encoded as a JSON string.
# with following keys: type, checksum, message, sequence number.
# This dictionary will represent our Packet structure.

import socket
import sys
import json
import random

MAX_NUM_OF_BYTES = 10000000
port = 6932
 
def client(host, port):        
    """Client program modeling TCP interaction with a server"""
    # Resolve the IP Address given the hostname and the port number using getaddrinfo
    

    try:
         add = socket.getaddrinfo(host,port,0,socket.SOCK_DGRAM,0,socket.AI_ADDRCONFIG| socket.AI_V4MAPPED)
         address = add[1][4]
         print( add)
    except socket.gaierror: 
        # insert error handling code because we couldn't resolve host name
         print("error for hostname")
         sys.exit()
         
    # Create a socket object with the proper socket specifications.
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
  

    seq = 0
    while True:
        # contains encoded message
        packet = {
           "message": "",
           "type": "ACK",
           "checksum": 0,
           "seq": 0
        }
        message = input("Enter your message:")
        
        #check the FIN
        if message == "FIN":
                #make the packet
                packet["type"]="FIN"
                packet["message"]=""
                packet["seq"]=0			
                #send to the server
                packets =json.dumps(packet)
                sock.sendto(packets.encode('ascii','ignore'), address)
                break
        else:
                #make the packet
                packet["type"]=""
                packet["message"]= message
                #emulating transmission of the network 
                if random.random()<0.5:
                        packet["checksum"]= -1
                else:
                        packet["checksum"]= sum(ord(char) for char in message)
                packet["seq"]= seq
                #send to the server
                packets =json.dumps(packet)
                sock.sendto(packets.encode('ascii', 'ignore'), address)

        while True:
                #receive the ack & decode
                receive, server_address = sock.recvfrom(MAX_NUM_OF_BYTES)

                receive= receive.decode('ascii', 'ignore')
                receive =json.loads(receive)
                if random.random()<0.5:
                    packet["checksum"]= -1
                else:
                    packet["checksum"]= sum(ord(char) for char in message)
                #check the sequence num
                if receive["seq"]== seq+1:
                        seq +=1
                        break
                else:
                        print("NO ACK!")
                        #resend the packet
                        packet["checksum"]= sum(ord(char) for char in message)
                        if random.random()<0.5:
                            packet["checksum"]= -1
                        else:
                            packet["checksum"]= sum(ord(char) for char in message)

                        packets =json.dumps(packet)
                        sock.sendto(packets.encode('ascii','ignore'), address)


    # Close the socket
    sock.close()
    
if __name__ == '__main__':
    if len (sys.argv) > 2:
        try:
            host = sys.argv[1]
            port = int(sys.argv[2])
            client (host, port)
        except:
            raise
    else:
        print ('Usage: python3 client.py host port')


