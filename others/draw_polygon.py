# draw_polygon.py
from turtle import *  # import all

def draw_polygon(number_of_sides,angle):
    for i in range(number_of_sides):
        forward(100)
        right(angle)
    return None
    
number_of_sides = int(input("Enter number of sides>"))
angle = 360 / number_of_sides
draw_polygon(number_of_sides,angle)
exitonclick()