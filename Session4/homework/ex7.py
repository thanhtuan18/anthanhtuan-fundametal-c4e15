flock = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Tuan and here is my flock")
print(flock)
print()
# y = max(flock)
print("Now my biggest sheep has size {0} let's shear it".format(max(flock)))

flock[flock.index(max(flock))] = 8
print()
print("After shearing, here is my flock")
print(flock)

for i in range(len(flock)):
    flock[i] = flock[i] + 50
print()
print("One month has passed, now here is my flock")
print(flock)
