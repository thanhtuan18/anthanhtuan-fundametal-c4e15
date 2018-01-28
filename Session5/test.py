#person = ["Tuan anh", 22, 2, "Hanoi", "Moc chau", 5, 4, "Maria", "Ping pong"]

# person = {}
# print(person)
#
# person = {
#     # key : value
#     "name": "Tuan anh"
# }
# print(person)

person = {
    # key : value
    "name": "Tuan anh",
    "age": 22,
    "sex": "male"
}

# for k in person:
#     print(k, person[k])
# if "age" in person:
#     print(person["age"])

# for k in person:
#     print(person[k])

# for k in person.values():
#     print(k)

# for key, value in person.items():
#     print(key, value)

# person["age"] +=1

# cach 1
for key in person:
    print(key, end=" ")
    print()

code = input("Your code? ")

if code in person:
    print(code, person[code])
else:
    new = input("Not found, do you want to contribute this word? (Y/N)?" )
    if new == "Y":
        new_key = input("Enter your translation: ")
        person[code] = new_key
        print("Updated")
