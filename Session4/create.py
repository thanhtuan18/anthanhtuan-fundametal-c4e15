print("Hi there, here you favorite things so far")

menu = ["death note", "netflix", "teaching"]
print(*menu, sep=', ')

y = input("Name one thing you want to add?" )
menu.append(y)
print(*menu, sep=', ')
