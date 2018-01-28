pair = []

for i in range(5):
    if i == 0:
        pair.append(1)
        print("Month {0}: {1} pair(s) of rabbit".format(i, pair[i]))
    elif i == 1:
        pair.append(2)
        print("Month {0}: {1} pair(s) of rabbit".format(i, pair[i]))
    else:
        pair.append(pair[i-2] + pair[i-1])
        print("Month {0}: {1} pair(s) of rabbit".format(i, pair[i]))
