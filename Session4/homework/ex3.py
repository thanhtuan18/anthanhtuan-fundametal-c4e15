items = ["T-Shirt", "Sweater"]

while True:
    x = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if x.upper() == "R":
        print("Our items: ", *items)
    elif x.upper() == "C":
        add_end = input("Enter new item: ")
        items.append(add_end)
        print("Our items: ", *items)
    elif x.upper() == "U":
        up_po = int(input("Update position? "))
        new = input("New item? ")
        items[up_po - 1] = new
        print("Our items: ", *items)
    elif x.upper() == "D":
        del_po = int(input("Delete position? "))
        items.pop(del_po - 1)
        print("Our items: ", *items)
    else:
        break
