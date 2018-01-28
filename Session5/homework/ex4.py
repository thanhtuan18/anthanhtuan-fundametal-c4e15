number = int(input("Enter a number: "))

count = 0
for i in range(number):
    if number % (i+1) == 0:
        count +=1

if count <= 2:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
