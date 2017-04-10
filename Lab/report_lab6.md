# Thida Aung
# Entropy Lab 6, COEN 146 L, Wed section 
# TA Arman Elahi


# Overview

In this section, describe what you did in this lab and how you accomplished it.
generate_file 
	It takes “file_name” in and write random char in it with 2^8 combinations of 8 bits and generates the most "random" file.
calculate_entropy
	This part calculates the entropy of that file based on the definition of Shannon Entropy. This method takes “file_name” and read the contents of the file to first calculate the frequency of each char in that contents . Then it calculate probability of each frequent char so it can eventually calculate entropy using shannon entropy formula at the end and return entropy at the end.

# Sources

http://stackoverflow.com/questions/700187/unicode-utf-ascii-ansi-format-differences
https://docs.python.org/2/library/random.html
Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object
https://docs.python.org/2/library/functions.html#ord
http://interactivepython.org/runestone/static/pip2/Functions/SideEffects.html
https://docs.python.org/3/library/argparse.html




# Methodology for generating random file

We were to generate random data and write into the file that we passed in as set up command line argument.
So I called random.randint () method to create first random integer then convert them into char and wrote those rand_char into the file with ‘w’ mode instead of ‘wb’ (write bytes) mode.

# Questions

    What sort of file will have higher entropy a normal text file or an encrypted text file?
- Encrypted text file will have higher entropy because it provides better security.

    UTF-8 another character encoding scheme takes 8 bits per character. What is the maximum achievable entropy for a file using all characters in UTF-8? How about for UTF-16?

- Since UTF-8 is variable length encoding, 1-4 bytes per code point while ASCII values are encoded as ASCII using 1 byte, the maximum achievable entropy for a file using all characters in UTF-8 would be 8 and it would be 16 for UTF-16. 

    Did you enjoy this lab? Was it helpful overall in your understanding of networks? 

- Yes, I learned a lot through report questions than the lab itself. In general, everything become to make sense only after the lab on what we actually trying to achieve, but I had no idea what I was doing during the lab.


# Extra Credit Completion

Put an X in the following boxes if you completed the extra credits. Please describe your general process for doing this. What sorts of changes did you have to make in running your program?

[] Implement generate_file in less than 8 lines, always achieving perfect entropy (of 8). 



# Comments and Feedback

