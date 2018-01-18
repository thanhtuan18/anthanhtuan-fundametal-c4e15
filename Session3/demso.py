# x = input("Enter a number: ")
# print(len(x))

# x = int(input("Enter a number: "))
# n = 1
# while True:
#     if ((x / (10**n)) > 10):
#         n += 1
#     else:
#         print(n+1)
#         break

x = int(input("Enter a number: "))
n = 0
# while True:
#     if x // 10 == 0:
#         print(n)
#         break
#     else:
#         x = x // 10
#         n += 1

while n > 0:
    n +=1
    n = n //10

print(n)
