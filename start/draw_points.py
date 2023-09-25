import turtle
import random

hight = 800
width = 900

turtle.setup(width + 15, hight + 15)
wn = turtle.Screen()

zolwik = turtle.Turtle()
zolwik.penup()      

size = 5

list = {f'p{i}': (random.randint(0,width/2), random.randint(0,hight/2)) for i in range(1, 4)}
list_of_points = list

zolwik.color("blue")
length = len(list_of_points.keys())
for i in range(1, length+1):
    zolwik.goto(list_of_points[f'p{i}'])
    zolwik.dot(size)

zolwik.goto((0,0))

turtle.Screen().exitonclick()