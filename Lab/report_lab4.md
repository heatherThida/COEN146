

# Thida Aung
# COEN 146L 
# Lab4 Report
# TA Arman (Wed session)

# Overview


Our goal is to create a socket object using UDP over IPv4 and able to send receive the data from stdin.
We start in server_lab4.py to open the socket and listen in client_lab4.py to echo out what the users type
by ::username ;;message format, until either of the users type “Quit” or ‘quit”. When we save users, we use python dictionary and if user is anonymous (meaning skipped ::username part and just type ;;message), IP address will be used. 
On the server side, it listen as long as hostname exist in dictionary users[], but upon “quit” message, delete users one by one. 
First, it didn't detect the "QUIT" string even I saw my argument return "True" upon seeing "quit or QUIT or words contain quit". Later, I found out it was because my if condition logic was opposite, after I negate it, so it should have been "Quit not in message _AND_ quit not in message" per Demorgan law, not _OR_. 


# Sources

http://pubs.opengroup.org/onlinepubs/009695399/functions/recvfrom.html
https://docs.python.org/2/library/socket.html
https://docs.oracle.com/cd/E19120-01/open.solaris/819-3000/ipconfig-22/index.html
http://docs.oracle.com/cd/E19253-01/816-4554/ipconfig-12/index.html

# Questions


From Lab4 week: 

1.) What does it mean that recvfrom() is a blocking function?
	Because If no messages are available at the socket and O_NONBLOCK is not set on the socket's file descriptor, recvfrom() shall block until a message arrives. If no messages are available at the socket and O_NONBLOCK is set on the socket's file descriptor, recvfrom() shall fail and set errno to [EAGAIN] or [EWOULDBLOCK].


2.) How would you implement a program that allows both the client and server to send and receive messages? So first the client would send, the server would receive. Then the server would send and the client would receive and so on. Don't need to actually implement, pseudocode is fine.

   sock.sendto(packets.encode('ascii','ignore'), address)
   data, address = sock.recvfrom(MAX_NUM_OF_BYTES)
   message= message.decode('ascii', 'ignore')	
    
   sock.sendto(packets.encode('ascii','ignore'), address)
   receive, server_address = sock.recvfrom(MAX_NUM_OF_BYTES)



3.) How does getaddrinfo() or gethostbyname() resolve the correct address? Hint: What Linux file are hosts stored in?
	Linux file are hosts stored in /etc/hosts/ and assigned default localhost IP addresses are used to configure the loopback interface. While getaddrinfo() converts names into a set of arguments to pass to the socket() and connect() syscalls, and gethostbyname() translate a host name to IPv4 address format and resolve the legacy to make the code becomes more portable. The IPv4 address then  is returned as a string, such as '100.50.200.5'. If the host name is an IPv4 address itself it is returned unchanged. These functions provide a useful interface for performing either of these name resolution operation, without having to deal with IPv4/IPv6 transparency.

4.) What is the loopback address?
	The IPv4 address 127.0.0.1 is the loopback address. The loopback address is the reserved network interface that is used by the local system to allow interprocess communication. This address enables the host to send packets to itself.

5.) How can you tell if the server has closed its connection?
	When we can no longer able to send or receive data through open socket since the remote has ended. In other word, recv return 0 when other side has closed.


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
