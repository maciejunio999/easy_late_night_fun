import turtle
import random

def middle(p1, p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

def calculate_middles(list_of_points):
    length = len(list_of_points.keys())
    result = {}
    n = 1
    for i in range(1, length):
        for j in range(i+1, length+1):
            print(i, j)
            result[f'pm{n}'] = middle(list_of_points[f'p{i}'], list_of_points[f'p{j}'])
            n+=1
    return result

def draw_points(turtle_f, color, size, points, what_point):
    length = len(points.keys())
    for i in range(1, length+1):
        turtle_f.color(color)
        turtle_f.goto(points[f'{what_point}{i}'])
        turtle_f.dot(size)

hight, width = 800, 900
half_h, half_w = hight/2, width/2

turtle.setup(width + 15, hight + 15)
wn = turtle.Screen()

zolwik = turtle.Turtle()
zolwik.penup()  
zolwik.speed('normal')    



list_of_points = {f'p{i}': (random.randint(-half_w, half_w), random.randint(-half_h, half_h)) for i in range(1, 4)}
list_of_middles = calculate_middles(list_of_points)

draw_points(zolwik, "blue", 10, list_of_points, 'p')
draw_points(zolwik, "red", 5, list_of_middles, 'pm')

zolwik.goto((0,0))

turtle.Screen().exitonclick()