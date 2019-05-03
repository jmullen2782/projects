'''
Created on Apr 4, 2019
Encrypted Message 1
@author: Jennie Mullen
'''
def main():
    text = input("Enter a file to encrypt: ")
def cipher():
    main()
    encrypt = open(text,"r")
    new = encrypt.read()
    new.close()
    import string
    alpha = []
    for c in string.ascii_lowercase:
        alpha.append(c)
    shift = 3
    code = []
    for i in range(0,26):
        code.append((i+shift)%26)
    newEncrypt = ''
    x = 0
    a = 0
    for character in encrypt[0:]:
        if encrypt[character] != alpha[a%26]:
            a += 1
        elif encrypt[character] == alpha[a]:
            newEncrypt.append=code[a], sep = ''
            x += 1
        elif encrypt[x].isupper():
            alpha.upper()
        elif encrypt[x].islower():
            alpha.lower()
    print(newEncrypt)
    test.ENC = open('new','w')
    print(new)