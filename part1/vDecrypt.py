#!/usr/bin/env python3

def vigDecrypt(ciphertext, key):
    decrypted = ''
    for i, ch in enumerate(ciphertext):
        decrypted += unshiftLetter(ch, key[i % len(key)])
    return decrypted

def unshiftLetter(letter, keyLetter):
    letter = ord(letter) - ord("A")
    keyLetter = ord(keyLetter) - ord("A")
    new = (letter - keyLetter) % 26
    return chr(new + ord("A"))

def listToString(s):
    str1 = " "
    for ele in s:
        str1 += ele
    return str1

if __name__ == '__main__':
    ctext = open("benctext.txt", "r").read().split("\n")
    ctext = listToString(ctext)
    #ctext = input("enter ciphertext: ").upper()
    ckey = input("enter key: ")
    output = vigDecrypt(ctext, ckey)
    print(output)