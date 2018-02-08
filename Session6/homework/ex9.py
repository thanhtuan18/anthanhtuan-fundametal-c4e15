def get_even_list(l):
    even = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
    return(even)

# a = get_even_list([1, 4, 5, -1, 10])
# print(a)
