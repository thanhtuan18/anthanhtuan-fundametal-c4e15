print ("Hi there, this is a superuser gateway")

for i in range(4):
    if i < 3:
        name = input("Username: ")
        if name == "c4e":
            Pass = input("Password: ")
            if Pass == ("123"):
                print("Wellcome, c4e")
                break
            else:
                print("Password is incorrect")
        else:
            print("You are not superuser")
    else:
        print("You filed to log in 3 times, go away")
        break
