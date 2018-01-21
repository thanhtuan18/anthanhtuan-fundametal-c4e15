word = ["champion", "meticulous", "hexagon"]

for i in range(len(word)):
    from random import randint          #chon 1 element bat ky trong list
    n = randint(0, len(word)-1)

    word_list = list(word[n])           #convert element da chon thanh list theo chu cai

    print("python word_jumble.py")

    for index in range(len(word_list)): #hien thi random tung chu cai trong list
        from random import randint
        n1 = randint(0, len(word_list)-1)
        print(word_list[n1], end=" ")
        word_list.pop(n1)

    print()
    guess = input("Your answer: ")
    if guess == word[n]:
        print("Hura")
    else:
        print(":(")

    word.pop(n)                          #xoa 1 element trong list
