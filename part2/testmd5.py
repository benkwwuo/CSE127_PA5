import sys, urllib.parse
from part2.pymd5 import md5, padding
from urllib.parse import urlparse

url = sys.argv[1]

#split url
prehash = url[:url.find("=")+1]
curhash = url[url.find("token")+6:url.find("token")+6+32]
print("length: " + str(len(curhash)))
msg = url[url.find("&")+1:]

print("Pre hash url: "+prehash)
print("Current hash: "+curhash)
print("Message string (without leading &): "+msg)

mlen = len(msg)+8 #assumes an 8 bit character password
bits = (mlen + len(padding(mlen*8)))*8
print("Message length in bits w/ secret key: ")
print(bits)

#establish new initialization vector and append command
#h = md5(state=curhash.decode("hex"), count=bits)
h = md5(state=bytes.fromhex(curhash), count=512)
x = "&command3=UnlockAllSafes" #sample appended command
h.update(x)

#generate new hash and url
newhash = h.hexdigest()
padding = urllib.parse.quote(padding(mlen*8))
print("Padding found at end of original instructions: "+padding)
msg = msg + padding + x

print("New hash to be inserted: "+newhash)

url = prehash+newhash+"&"+msg

print("New url is: ")
print(url)
