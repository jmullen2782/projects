'''
Created on Apr 4, 2019

@author: Jennie Mullen
'''
def cipher():
    text = input("Please enter a file name: ")
    encrypt = open(text,"r")
    new = encrypt.read()
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
    for character in encrypt:
        if encrypt[x] != alpha[a%26]:
            a += 1
        elif encrypt[x] = alpha[a]:
            newEncrypt.append=code[a], sep = ''
            x += 1
        elif encrypt[x].isupper():
            alpha.upper()
        elif encrypt[x].islower():
            alpha.lower()
    print(newEncrypt)
    test.ENC = open('new','w')
    print(new)