# Lab7 Diffie Hellman Algorithm
# Thida Aung Wed Lab (TA: Arman E)


import math


p = int(input("Enter your 1st prime number: ") )#Request user for (shared) 1st prime
g = int(input("Enter your 2nd prime number: ")) #Request user for (shared) 2nd prime  
a = int(input("Please enter first private key: ")) #Request user for Jill's private key
b = int(input("Please enter second private key: ") )#Request user for Bill's private key

#calculate public keys
A = pow(g,a, p )
B = pow(g,b,p)
S1 = pow(B,a,p)
S2 = pow(A,b,p)

if (S1 == S2):
    print("Your shared secret key is {}" .format(S1) )


def isPrime(n):
  #Function for checking if p and g are prime
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def isInt(n):
  #Function for checking if secret is an integer
    return type(1) == type(n)


if not isPrime(p):
    print ("Your number is not prime...")
    exit()
if not isPrime(g):
    print ("Your number  is not prime...")
    exit()
if not isInt(a):
    print ("Your private key is not an integer...")
    exit()
if not isInt(b):
    print ("Your private key is not an integer...")
    exit()
