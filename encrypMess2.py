'''
Created on Apr 10, 2019

@author: jmullen19
'''
def caesar_cipher(fname, encrypt, shift):
    fname = input("Please enter a file name: ")
    file = open(fname,"r")
    new = file.read()
    new.close()
    import string
    alpha = []
    for c in string.ascii_lowercase:
        alpha.append(c)
    shift = int(input("How many places would you like to shift?"))
    code = []
    for i in range(0,26):
        code.append((i+shift)%26)
    newEncrypt = ''
    x = 0
    a = 0
    for character in file[0:]:
        if file[character] != alpha[a%26]:
            a += 1
        elif file[character] = alpha[a]:
            newEncrypt.append=code[a], sep = ''
            x += 1
        elif file[x].isupper():
            alpha.upper()
        elif file[x].islower():
            alpha.lower()
    print(newEncrypt)
    test.ENC = open('new','w')
    print(new)