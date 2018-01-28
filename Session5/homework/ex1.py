data = input("Enter your data: ")
data2 = list(data.lower())

alpha = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "y": 0,
    "w": 0,
}

for k, v in alpha.items():
    for i in data2:
        if k == i:
            v += 1
    if v >= 1:
        print(k, v)
