# Bai 1
# teencode = {
#     "ng": "Người, Nói về con người, một người nào đó hoặc nói chung về người",
#     "pt": "Phát triển, biết một điều...",
#     "r": "Rồi, ý nói đã xong một việc gì đó"
# }
#
# y = input("Your code? ")
#
# if y in teencode:
#     print("Translation:", teencode[y])
# else:
#     print("Not found")

# Bai 2
code_dict = {
    "any": "Anh người yêu",
    "eny": "Em người yêu"
    }

while True:
    for key in code_dict:
        print(key, end=" ")
    print()

    code = input("Enter a code? ")

    if code in code_dict:
        print(code_dict[code])
    else:
        print("Not found")
        contribute = input("Add this code (Y/N)? ")
        if contribute.lower() == "y":
            translation = input("Enter translation: ")
            code_dict[code] = translation
