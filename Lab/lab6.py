# Thida Aung COEN 146L
# lab 6 (TA: Arman -Wed session) 
# Entropy and Information Theory by generating the most "random" file we can have and
# calculating the entropy of that file based on the definition of Shannon Entropy.


import argparse
import math
import random

def generate_file(file_name):
    """
    Here's my docstring for my generate file. If this doesn't get filled in I get - 5.   
    Positional Arguments: This generate_file method takes the file name as part of the set up argument
    in command line when we test "generate" or "main"  and write random characters into it
    Side Effects: There's side effects on what file name we pass in, since we are passing file_name as parameter. For example,
    if we pass in the existing filename in our directory, it will overwrite it and modified into a random generated char.
    """

    # For iteration in number of random ints to generate
    #   generate random int and  write ,
    with open(file_name, 'w') as f:
        for i in range(255):
            f.write(chr(random.randint(0, 255))) 


def calculate_entropy(file_name):
    """
    Here's my docstring for my calculate entropy. If this doesn't get filled in I get - 5.   
    Positional Arguments: This calculate_entropy method takes the file name as part of the set up argument
    in command line when we test "calculate" or "main" and read the file contents
    Side Effects: The function is not mutating any states so there's no side effects, meaning we are not modifying
    the file we passed in.We only read the content and return the entropy value
    """
    # chr_counts['a'] = number of times I have seen 'a'
    # index of 'a' = int('a')
    chr_counts = [0] * 256
  
    
    #file = open(file_name, 'r')
    file_contents = open(file_name, 'r').read()
    filesize = len(file_contents)
    for k in file_contents:
        freq_index = ord(k) #str to int conversion is done by ord so [a,a,b,c] => [97,97,98,99]
        chr_counts[freq_index] += 1

    entropy = 0     
    for freq in chr_counts:
        if freq > 0:
            #convert frequency array entry -> probabiliy distribution
            prob = float(freq)/ filesize
            # shannon entropy formula
            entropy += prob * math.log(prob,2)
    entropy = -entropy
    print ('Calculate Entropy: ', entropy)
    return entropy



## DO NOT NEED TO EDIT ANYTHING UNDER HERE
# setup command line options
parser = argparse.ArgumentParser(description='Generate a random file and calculate its Shannon Entropy')
parser.add_argument('-e', '--execute', dest='fxn', help='Function to be executed: calcaulte, generate, main')
parser.add_argument('-f', '--file', default='lab6.txt', dest='file_name', help='File to either calculate entropy or generate into')

args = parser.parse_args()

if args.fxn == 'generate':
    generate_file(args.file_name)
elif args.fxn == 'calculate':
    calculate_entropy(args.file_name)
elif args.fxn == 'main':
    generate_file(args.file_name)
    calculate_entropy(args.file_name)
else:
    parser.print_help()

