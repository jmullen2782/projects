'''
Created on Apr 4, 2019

@author: Jennie Mullen
'''
import string
alpha = []
for c in string.ascii_lowercase:
    alpha.append(c)
code = []
count = 0
for i in range(0,26):
    code.append((count+i)%26)
    count+=1
shift = -3
alpha.insert(0,alpha[shift:])
del alpha[shift:]
text = input("Please enter a file name: ")
encrypt = open(text,"r")

    
        
        
    