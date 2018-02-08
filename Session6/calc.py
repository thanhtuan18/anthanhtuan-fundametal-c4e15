def eval(x, y, op):

    result = 0
    if  op =="+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    else:
        result = x / y

    return result

# x = int(input("x = "))
# y = int(input("y = "))
# op = input("op = ")
#
# result = eval(x, y, op)
# print("{0} {1} {2} = {3}".format(x, op, y, result)) # sinh ra và chết trong eval



# x = int(input("x = "))
# ope = input("Operator(+,-,*,/): ")
# y = int(input("y = "))
#
# result = 0
#
# if ope == "+":
#     result = x + y
# elif ope == "-":
#     result = x - y
# elif ope == "*":
#     result = x * y
# else:
#     result = x / y
#
# print("{0} {1} {2} = {3}".format(x, ope, y, result))
