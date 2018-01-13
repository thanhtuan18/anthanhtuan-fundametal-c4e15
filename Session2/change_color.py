# from turtle import *
#
# speed (0)
#
# color ("green")
# forward (100)
# color ("red")
# forward (100)
#
# mainloop ()

from turtle import *

speed (0)
width (5)

for i in range (3):
    color ("red")
    forward (20)
    penup ()
    forward (20)
    pendown ()
    color ("blue")
    forward (20)
    penup ()
    forward (20)
    pendown ()

mainloop ()
