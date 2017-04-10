# Overview

During this lab, we designed a Stop and Go protocol to send and receive packets between the client and the server.  We also implemented a method to identify each packet and ensure the correctness of the message sent in the packet by using checksum.
The flow of the lab is as follow:

Client:
- ask users to enter a message
- check is the message is FIN
	- if it is, break and send the packet
	- if it is not, compute the checksum, make the packet, and send it to the server
-receive the ACK from the server
-check the seq number
-send a gain

Server:
- receive the message from the user
- check if the message is FIN
	- Yes: quit
	- No: check the checksum
- If the checksum equals to the checksum in the message
	- Yes: increase the sequence number
	- NO: ask the client to resend the message
# Sources

- Arman (because he's very very awesome LOL)
- stackoverflow ....
- https://docs.python.org/2/library/json.html

# Questions

Type your answers to the following questions on a new line after each question.

If the current sequence number is 5, what should your sequence number be if the server received the incorrect checksum? What 
should it be if your server received the correct checksum
	
- The sequence number should still be 5 since it needs to resend No.5 packet.
- If the server receives the correct checksum, the seq number should be 6

How could we ensure the packets were delivered to the application in the correct order while allowing the client to not be blocked by a recvfrom call? (No code, just ideas). What sort of protcol could we use?

 - before clients sends packets to the sever,it should assign each of the packets with sequence number (ex: 1,2,3,4....n). After sending all the packets, the server will reassign them into the correct order based on the sequence number.

What are some other ways besides checksums to check the correctness of packets?

- two-dimentional parity
- cyclic redeundancy check

# Extra Credit Completion

Put an X in the following boxes if you completed the extra credits. Please describe your general process for doing this. What sorts of changes did you have to make in running your program?

[] Implement Go Back N Protocol for TCP and asynchronous

# Questions For TA
N/A

# Comments and Feedback
N/A