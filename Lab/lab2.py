# -*- coding: utf-8 -*-
# Thida Aung
# COEN 146 lab2 a program to generate the data.log of runtime per each different file size on network using 
# time cat ~/lab2.txt|head -c 0MB|ssh taung@linux.scudc.scu.edu "(cat -> ~/COEN146/)"

import subprocess

megs = 10**6
with open("data.log", 'w') as outfile:
    for file_size in range (0,1000*megs,100*megs):
        for run_num in range(10):
            subprocess.call('>&2 echo for file size: {}'.format(file_size),stderr = outfile, shell= True)
            subprocess.call('time cat ~/COEN146/lab2.txt|head -c {}|ssh -q taung@linux.scudc.scu.edu "(cat -> ~/COEN146/lab2copy.txt)"\n '. format(file_size),stderr = outfile, shell= True )

