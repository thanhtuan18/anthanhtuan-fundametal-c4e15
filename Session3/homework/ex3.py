print("Guess your number game")
print("Now think of a number from 0 to 100, then press 'Enter'")
print("All you have to do is to answer to my guess")
print("'c' if my guess is 'C'orrect")
print("'s' if my guess is 'S'maller than your number")
print("'l' if my guess is 'L'arger than your number")

lo = 0
hi = 100
loop = True

# while loop:
#     mid = (lo + hi) // 2
#     answer = input("Is" + str(mid) + "your number")
#     if answer.lower() == 'c':
#         print("I knew it")
#         loop = False
#     elif answer.lower() == 's':
#         hi = mid
#     elif answer.lower() == 'l':
#         lo = mid


while loop:
    mid = (lo + hi) // 2
    answer = input("Is {0} your number".format(mid))
    if answer.lower() == 'c':
        print("I knew it")
        loop = False
    elif answer.lower() == 's':
        hi = mid
    elif answer.lower() == 'l':
        lo = mid



# cu

# print("Guess your number game")
# print("Now think of a number from 0 to 100, then press 'Enter'")
# print("All you have to do is to answer to my guess")
# print("'c' if my guess is 'C'orrect")
# print("'s' if my guess is 'S'maller than your number")
# print("'l' if my guess is 'L'arger than your number")

# x = 50
# for i in range (10):
#     print("Is", x, "your number?", end="")
#     y = input()
#     if y == "s":
#         x = int(x + (50 / (2**(i+1))))
#     elif y == "l":
#         x = int(x - (50 / (2**(i+1))))
#     else:
#         print("I knew it")
#         break
