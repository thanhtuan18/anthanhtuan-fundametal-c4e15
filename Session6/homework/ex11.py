def is_inside(x1, y1, x2, y2, w, h):
    if ((x2 + w) >= x1 >= x2 ) and ((y2 + h) >= y1 >= y2):
        return(True)
    else:
        return(False)

# c = is_inside(100, 120, 140, 60, 100, 200)
# print(c)
