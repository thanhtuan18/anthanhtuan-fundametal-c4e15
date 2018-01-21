#TH1:
# print("Hi there, here you favorite things so far")
# menu = ["death note", "netflix", "teaching"]
# # print(*menu, sep=", ")
#
# for i in range(len(menu)):
#     # print(i+1, ".", end="")
#     print("{0}. ".format(i+1), end="")
#     print(menu[i])

    # print("{0}. {1}".format(i, menu))

#TH2:
favs = ["teaching", "net"]
# n = 1
# for i in favs:                      #foreach
#     print("{0}. {1}".format(n, fav))
#     n += 1

#TH3:
for index, fav in enumerate(favs):
#     print(str(index + 1) + ".", fav)
#
# print(*enumerate(favs))

#TH4:
    s = "{0}. {1}".format(index + 1, fav)
    print(s)
