#TH1
# print("Hi there, here you favorite things so far")
#
# menu = ["death note", "netflix", "teaching"]
# for index, data in enumerate(menu):
    # print(str(index + 1) + ".", data)
#
# de_num = int(input("Favorite position you want to del: "))
# menu.pop(de_num-1)
#
# for index, data in enumerate(menu):
    # print(str(index + 1) + ".", data)
#
# print("Hi there, here you favorite things so far")

#TH2
menu = ["death note", "netflix", "teaching"]
for index, data in enumerate(menu):
    print(str(index + 1) + ".", data)

de_num = input("Favorite position you want to del: ")
menu.remove(de_num)

for index, data in enumerate(menu):
    print(str(index + 1) + ".", data)
