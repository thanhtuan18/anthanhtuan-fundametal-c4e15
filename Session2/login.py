print("Hi there, this is a superuser gateway")

from getpass import getpass

x = input("Usernam: ")

if x == "c4e":
    y = getpass("Password: ")
    if y == "codethechange":
        print ("Well come, c4e")
    else:
        print ("Password is incorrect")
else:
    print ("You are not superuser")
