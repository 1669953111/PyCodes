from turtle import *  # import all
from itertools import cycle

colors = cycle(['red','orange','yellow','green','blue','purple'])

def draw_circle(size,angle,shift):
    pencolor(next(colors))
    circle(size)
    right(angle)
    forward(shift)
    draw_circle(size+5,angle+1,shift+1)

bgcolor("black")
speed("fastest")
pensize(4)
draw_circle(30,0,1)