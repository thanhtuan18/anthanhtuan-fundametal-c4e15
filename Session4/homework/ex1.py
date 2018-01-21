from turtle import *

colors = ["red", "blue", "brown", "yellow", "grey"]
speed(0)

for canh in range(3, len(colors)+3):
    color(colors[canh-3])
    for y in range(canh):
        forward(100)
        turn = ((canh-2)*180)/(canh) #tinh 1 goc da giac deu la bao nhieu do
        left(180-turn)

mainloop()
