from random import randint, choice
from calc import eval

x = randint(0, 10)
y = randint(0, 10)
op = choice(["+", "-", "*", "/"])
error = randint(-1, 1)

display_result = eval(x, y, op) + error

print("{0} {3} {1} = {2}".format(x, y, display_result, op))

answer = input("Y/N? ").lower()

if (answer == "y" and error == 0) or (answer != "y" and error != 0):
    print("Yeah")
else:
    print("No")
