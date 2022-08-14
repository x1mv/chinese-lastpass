##MAKE SURE TO PUT THIS IN A FOLDER BEFORE YOU LAUNCH IT
##OR IF YOU HAVE A PASSWORD.TXT FILE ALREADY PLACE IT
##SOMEWHERE ELSE AS THIS WILL REWRITE IT


##x1mv\\2022\\projectname;chineselastpass;version:1.0\
import secrets
import uuid
import os.path
import random
import string



version = "1.1"


f = open("password.txt", "w")
file_exists = os.path.exists('password.txt')
## was only here 4 debugging -> print("password file exists")
print("chineselastpass | version",version)
print("uuid or hex")
mode = input("choose mode: ")

if mode == "uuid":
    uuidSTRING = uuid.uuid4()
    print("your unique uuid pass: ", uuidSTRING)
    print("output to folder. please check the \n directory where this .py file is.")
    f.write(str(uuidSTRING))
    f.close()
elif mode == "hex":
    hexSTRING = secrets.token_hex(32)
    print("your unique hexadecimal pass: ", hexSTRING)
    print("output to folder. please check the \n directory where this .py file is.")
    f.write(str(hexSTRING))
    f.close()
x = input("press enter to exit")
