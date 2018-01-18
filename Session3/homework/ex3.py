print("Guess your number game")
print("Now think of a number from 0 to 100, then press 'Enter'")
print("All you have to do is to answer to my guess")
print("'c' if my guess is 'C'orrect")
print("'s' if my guess is 'S'maller than your number")
print("'l' if my guess is 'L'arger than your number")

x = 50
for i in range (10):
    print("Is", x, "your number?", end="")
    y = input()
    if y == "s":
        x = int(x + (50 / (2**(i+1))))
    elif y == "l":
        x = int(x - (50 / (2**(i+1))))
    else:
        print("I knew it")
        break
