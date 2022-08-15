##MAKE SURE TO PUT THIS IN A FOLDER BEFORE YOU LAUNCH IT
##OR IF YOU HAVE A PASSWORD.TXT FILE ALREADY PLACE IT
##SOMEWHERE ELSE AS THIS WILL REWRITE IT


##x1mv\\2022\\projectname;chineselastpass;version:1.2\
import secrets
import uuid
import os.path
import random
import string



version = "1.2"


f = open("password.txt", "w")
file_exists = os.path.exists('password.txt')

def save(type):
    f.write(type)
    f.close()

## was only here 4 debugging -> print("password file exists")
print("chineselastpass | version",version)
print("uuid, hex or unsafe")
mode = input("choose mode: ")

if mode == "uuid":
    uuidSTRING = uuid.uuid4()
    print("your unique uuid pass: ", uuidSTRING)
    print("output to folder. please check the \n directory where this .py file is.")
    save(str(uuidSTRING))
elif mode == "hex":
    hexSTRING = secrets.token_hex(32)
    print("your unique hexadecimal pass: ", hexSTRING)
    print("output to folder. please check the \n directory where this .py file is.")
    save(str(hexSTRING))
elif mode == "unsafe":
    lower = "abcdefghijklmnopqrstuvxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    number = "0123456789"
    symbol = ">#&@{}<;>?:_.,-[]/\'"
    usable = lower + upper + number + symbol
    lenght = 16
    password = "".join(random.sample(usable, lenght))
    print("your unsafe 16char password is: ", password)
    print("output to folder. please check the \n directory where this .py file is.")
    save(password)

x = input("press enter to exit")
