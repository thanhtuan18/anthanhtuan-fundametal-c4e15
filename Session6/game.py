from random import randint

x = randint(0, 10)
y = randint(0, 10)
z = x + y + randint(-1, 1)

print("{0} + {1} = {2}".format(x, y, z))

result = input("(Y/N)? ")

if x + y == z and result.lower() == "y":
    print("Yay")
elif x + y != z and result.lower() == "y":
    print("Wrong")
elif x + y != z and result.lower() == "n":
    print("Yay")
elif x + y == z and result.lower() == "n":
    print("Wrong")
else:
    print("Error")
