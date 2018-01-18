# cot = int(int(input("Dien so cot: ")) / 2)
# dong = int(input("Dien so dong: "))
#
# for i in range (dong):
#     x = cot * "X*"
#     print(x)

col = 4
row = 4
for y in range(row):
    for x in range(col):
        if (x + y) % 2 == 0:
            print("X", end=" ")
        else:
            print("*", end=" ")
    print()
