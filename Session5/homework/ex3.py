numbers = [1, 6, 8, 1, 2, 1, 5, 6]

count = 0

number = int(input("Enter a number? "))
for i in numbers:
    if number == i:
        count +=1
print("{0} appears {1} times in my list".format(number, count))
