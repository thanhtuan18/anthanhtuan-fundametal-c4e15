from turtle import *

colors = ["red", "blue", "brown", "yellow", "grey"]
speed(0)

for i in range(len(colors)):
    color(colors[i])
    for canh in range(2):
        begin_fill()
        right(90)
        forward(100)
        right(90)
        forward(50)
        end_fill()
    penup()
    forward(50)
    pendown()

penup()
backward(50)
pendown()

mainloop()
