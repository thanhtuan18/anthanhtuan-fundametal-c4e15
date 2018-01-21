word = "champion"
word_list = list(word)                  #convert string sang list

print("python word_jumble.py")

for index in range(len(word_list)):
    from random import randint          #chon random 1 chu cai trong list
    n1 = randint(0, len(word_list)-1)
    print(word_list[n1], end=" ")
    word_list.pop(n1)                   #xoa bot 1 elment trong list

print()
guess = input("Your answer: ")
if guess == word:
    print("Hura")
else:
    print(":(")
