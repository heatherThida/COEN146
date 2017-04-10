# Lab5
# COEN 146L (Wed) Thida Aung 
# TA. Arman Elahi
# Stop and Go Packet Transfer Report

# Overview

This lab goal is to implement a partial TCP implementation by keep transferring messages until we get a FIN packet. We identify each packet and ensure FIFO ordering as well as ensuring the correctness of the message to act as TCP.
The flow of the lab is as follow:

Client:
- create packet with 4 field declaration (message, type, checksum, seq)  
- ask users to enter a message
- check is the message is FIN
	- if it is, break and send the packet after encoded
	- if it is not, compute the checksum, make the packet, and send it to the server
		- compute checksum by adding all the char in the messages 
While true     
	-receive the ACK from the server, (decode everytime we receive) 
	-check the seq number (add 1 if ACK received, don’t add 1 if NO ACK) 
	-send a gain (encoded everytime we send) but try using random function to see the failures and success in random time 
After all sent, close the socket 



Server:
- receive the message from the user, decode the message and load them as json objects into data 
- check if the message is FIN
	- Yes: print final message and break
	- No: check the checksum with sum(ord(c) for c in data[]) functiton 
        - If the checksum equals to the checksum in the message
	      - Yes: prepare the packet by setting “type” as “ACK”, increase the seq number and print the message
	      - NO: ask the client to resend the message and print the message 

After all  receive and sent, close the socket. 


# Sources

http://beej.us/guide/bgnet/output/html/multipage/syscalls.html#sendtorecv
https://docs.python.org/2/library/json.html

# Questions


If the current sequence number is 5, what should your sequence number be if the server received the incorrect checksum? What should it be if your server received the correct checksum?
	
	The sequence number should be still no# 5 since it needs to resend that no#.5 packet if the server received the incorrect checksum. If the server receives the correct checksum, the seq no# should be 6.

How could we ensure the packets were delivered to the application in the correct order while allowing the client to not be blocked by a recvfrom call? (No code, just ideas). What sort of protocol could we use?

	TCP protocol made sure the packets were delivered to the application in the correct order while allowing the client to not be blocked by a recvfrom call. Client should assign each of the packets with sequence number (ex: 1,2,3,4....n) before clients sends packets to the sever. After sending all the packets, the server will reassign them into the correct order based on the sequence number. 

What are some other ways besides checksums to check the correctness of packets?
       
	- two-dimensional parity
	- cyclic redundancy check
are the two other ways besides checksums.


# Extra Credit Completion

Put an X in the following boxes if you completed the extra credits. Please describe your general process for doing this. What sorts of changes did you have to make in running your program?

[] Implement Go Back N Protocol for TCP and asynchronous

# Questions For TA

If you have any questions, just start typing them here. I gave you one to start off with. These are’nt necessary

1. Is this stuff actually ever used/ is it useful?
  Yes, this is very interesting and useful. 

# Comments and Feedback

If you have anything you’d like to tell me about, go ahead and write it in here. If its a GIF you want me to use or some thesis on why I suck, thats cool. Just remember that I control your grade for this lab.
