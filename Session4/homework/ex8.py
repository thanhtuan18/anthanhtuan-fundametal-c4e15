flock = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Tuan and here is my flock")
print(flock)

for month_loop in range (3):
    print()
    print("MONTH {0} :".format(month_loop+1))

    for i in range(len(flock)):
        flock[i] = flock[i] + 50
    print("One month has passed, now here is my flock")
    print(flock)

    print("Now my biggest sheep has size {0} let's shear it".format(max(flock)))

    flock[flock.index(max(flock))] = 8
    print("After shearing, here is my flock")
    print(flock)
