##MAKE SURE TO PUT THIS IN A FOLDER BEFORE YOU LAUNCH IT
##OR IF YOU HAVE A PASSWORD.TXT FILE ALREADY PLACE IT
##SOMEWHERE ELSE AS THIS WILL REWRITE THE SHIT OUT OF IT


##x1mv\\2022\\projectname;chineselastpass;version:1.0\

import random,secrets,os,binascii


version = "1.0"

f = open("advancedpassword.txt", "w")
file_exists = os.path.exists('advancedpasswordpassword.txt')
print("chinese lastpass {ADVANCED} | version", version)
print("randombits, urlsafe or binascii")
mode = input("choose mode: ")

if mode == "randombits":
    hexrand = hex(random.getrandbits(128))
    print("your unique randombit password is:",hexrand)
    print("output to folder. please check the \n directory where this .py file is. (advancedpassword.txt)")
    f.write(str(hexrand))
    f.close()
elif mode == "urlsafe":
    urlsafe = secrets.token_urlsafe(22)
    print("your unique urlsafe password is:",urlsafe)
    print("output to folder. please check the \n directory where this .py file is. (advancedpassword.txt)")
    f.write(str(urlsafe))
    f.close()
elif mode == "binascii":
    binascii = binascii.b2a_hex(os.urandom(15))
    print("your unique binascii password is:",binascii)
    print("output to folder. please check the \n directory where this .py file is. (advancedpassword.txt)")
    f.write(str(binascii))
    f.close()
x = input("press enter to exit")
