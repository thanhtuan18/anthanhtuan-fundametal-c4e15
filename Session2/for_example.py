# for _ in range(2, 8, 3):
#     print("Hi")
# print("Bye")

# for i in range(2, 8, 3):
#     print("Hi")
# print("Bye")

# for i in range(2, 8):
#     print("Hi")
# print("Bye")

# x = 5
# for i in range(x):
#     print(i)


# n = int(input ("Enter a number: "))
# for i in range(n):
#     print(i)


# n = int(input("Enter a number: "))
# for i in range (0, n, 2):
#     print(i)


from turtle import *

shape("turtle")
speed(0)

for i in range (2, 300, 2):
    forward (2 + i)
    left (90)

mainloop()
