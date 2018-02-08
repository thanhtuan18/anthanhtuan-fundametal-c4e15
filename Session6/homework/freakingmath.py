from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0, 10)
    y = randint(0, 10)
    op = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)
    if op == "+":
        result = x + y + error
    elif op == "-":
        result = x - y + error
    elif op == "*":
        result = x * y + error
    else:
        result = x / y + error
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    pass
    #return True (hoac faul)
