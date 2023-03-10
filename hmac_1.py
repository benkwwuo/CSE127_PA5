from pymd5 import md5, padding

m = "Use HMAC, not hashes"
x= "Good advice"
h = md5()
h.update(m)
print("Use HMAC, not hashes = " + h.hexdigest())

h = md5()
h.update(m)
print(h.hexdigest())
h.update(x)
print("h:  ", h.hexdigest())


# method 2
h2 = md5(state=bytes.fromhex("3ecc68efa1871751ea9b0b1a5b25004d"), count=512)
h2.update(x)
print("h2: ", h2.hexdigest())

# method 3
h3 = md5()
h3.update(m+x)
print("h3: ", h3.hexdigest())

# method 4
new_m = m.encode("utf-8") + padding(len(m)*8) + x.encode("utf-8")
print("h4: ", md5(new_m).hexdigest())

url = "http://bank.cse127.ucsd.edu/pa5/api?token=d6613c382dbb78b5592091e08f6f41fe&user=nadiah&command1=ListSquirrels&command2=NoOp"
urlExt = "&command3=UnlockAllSafes"

