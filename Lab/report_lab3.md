

# Thida Aung
# COEN 146L 
# Lab3 Report
# TA Arman (Wed session)

# Overview

Our goal is to transfer data via datagrams after we create UDP socket using socket program template. The Client open and read a file we passed in and transfer it line by line to our Server. First, we expect a datagram that has filename so we can open it to start writing. Then we tried to send a encoded message from client side while you server is waiting. Upon receipt, server decode all the data as ascii so we can properly write out to the file. Then we give it a new file name and copied those data and write in that file until we see “” string. 

# Sources

https://docs.python.org/2/howto/sockets.html
https://docs.python.org/3.5/library/socket.html
http://www.techbeamers.com/python-tutorial-essentials-of-python-socket-programming/#h1


# Questions

From Lab3 week: 

1. Describe UDP in your own words.
User Datagram Protocol is a connectionless protocol that demultiplexes packets and queues them at each port.  Because UDP provides port numbers, we can identify different users by their port numbers, allowing us to verify that the checksum of the data arrived intact.
		There are 6 main properties of TCP: 
    1. reliable, in order
    2. connection oriented
    3. paired byte streams (2 way flow)
    4. flow control
    5. demultiplexing (multiple app support)
    6. congestion control


2. What does the bind function do? Do we need it on the client?
	Bind function attaches host and port together for the first time to tell the receiver that’s ok to establish sending and receiving. No, we do not need it on the client again.
 
3. In your own words, describe what a socket is.
  	A socket serve as a telephone or a container that holds IP address and port number after two ends has started bidirectional communication.

4. What are the pieces used to create a socket. What is each one for?
	They are socket_family, socket_type, and protocol, which are also the parameters we used for socket.socket() method.
Family -  tells which protocols we used either AF_INET, AF_INET6, AF_UNIX, AF_CAN or AF_RDS as the transport mechanism. 
Type -   tells the types of communication between the two end-points with either SOCK_STREAM (for connection-oriented protocols e.g. TCP), or SOCK_DGRAM (for connectionless protocols e.g. UDP) or SOCK_RAW. 
Proto - usually set to 0 except in the case where the address family is AF_CAN the protocol should be 1.


5. What are the Address, Family, Host, and Port variables used for in creating a socket
	Address variable tells the address we are connecting to, Family variable is for the type of address such as IPv4, IPv6, Host variable represents the hostname in internet domain such as localhost, machine no# we are using. and Port variable is an integer no# used like a house address no# to tell which house no# we are delivering our packets to.


# Extra Credit Completion

Put an X in the following boxes if you completed the extra credits. Please describe your general process for doing this. What sorts of changes did you have to make in running your program?

[] Transfer a text file to your neighbor
[] Transfer an image file to your TA

# Questions about the class

1. Do you feel like you have enough Python knowledge to complete this lab?
  yes, after the lab.
2. Do you actually understand what we did in this lab?
  yes, also after the lab.
3. Do the templates and stuff help? How could they be improved (No I will not just give you all the correct code)
  definitely, especially flow chart to tell where to start.
