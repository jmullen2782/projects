'''
Created on Apr 10, 2019
Encrypted Message 2
@author: Jennie Mullen
'''
def main():
    fname = input("Enter a file to encrypt/decrypt: ")
    shift = int(input("How many places should the alphabet be shifted?"))
    encrypt = input("Would you like to encrypt or decrypt a file?")
   
def caesar_cipher(fname, encrypt, shift):
    import string
    alpha = []
    for c in string.ascii_lowercase:
        alpha.append(c)
    newalpha = []
    main()
    if encrypt.lower() == "encrypt":
        for i in alpha:
            newalpha.append((i+shift)%26)
        newEncrypt = ''
        x = 0
        a = 0
        for character in fname[0:]:
            if fname[character] != alpha[a%26]:
                a += 1
            elif fname[character] = alpha[a]:
                newEncrypt.append=newalpha[a], sep = ''
                x += 1
            elif fname[x].isupper():
                alpha.upper()
            elif fname[x].islower():
                alpha.lower()
    else:
        shift  *=-1
        for i in alpha:
            newalpha.append((i+shift)%26)
        newEncrypt = ''
        x = 0
        a = 0
        for character in fname[0:]:
            if fname[character] != alpha[a%26]:
                a += 1
            elif fname[character] = alpha[a]:
                newEncrypt.append=newalpha[a], sep = ''
                x += 1
            elif fname[x].isupper():
                alpha.upper()
            elif fname[x].islower():
                alpha.lower()
    print(newEncrypt)
    test.ENC = open('new','w')
    print(new)
    