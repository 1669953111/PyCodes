from turtle import *
from random import randint, random

def draw_star(points,size,col,x,y):
    penup()
    goto(x,y)
    pendown()
    angle = 180 - (180 / points)
    color(col)
    begin_fill()
    for i in range(points):
        forward(size)
        right(angle)
    end_fill()

# main code
Screen().bgcolor("dark blue")
speed(0)

while True:
    points = randint(2,5) * 2 + 1
    size = randint(10,50)
    col = (random(),random(),random())
    x = randint(-350,300)
    y = randint(-250,250)

    draw_star(points,size,col,x,y)