import turtle
import random


def area(list_of_points):
    return 0.5 * abs(
        ((list_of_points['p2'][0] - list_of_points['p1'][0]) * 
         (list_of_points['p3'][1] - list_of_points['p1'][1])) - 
        ((list_of_points['p2'][1] - list_of_points['p1'][1]) * 
         (list_of_points['p3'][0] - list_of_points['p1'][0])))


def middle(p1, p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)


def calculate_middles(list_of_points):
    length = len(list_of_points.keys())
    result = {}
    n = 1
    for i in range(1, length):
        for j in range(i+1, length+1):
            result[f'pm{n}'] = middle(list_of_points[f'p{i}'], list_of_points[f'p{j}'])
            n+=1
    return result


def draw_points(turtle_f, color, size, points, what_point):
    length = len(points.keys())
    for i in range(1, length+1):
        turtle_f.color(color)
        turtle_f.goto(points[f'{what_point}{i}'])
        turtle_f.dot(size)


def draw_lines(turtle_f, color, cor_for_lines):
    for i in range(0, 3):
        points = cor_for_lines[i]
        turtle_f.color(color)
        turtle_f.goto(points[0])
        turtle_f.pendown()
        turtle_f.goto(points[1])
        turtle_f.penup()

def draw_sides(turtle_f, color, points):
    length = len(list_of_points.keys())
    for i in range(1, length):
        for j in range(i+1, length+1):
            turtle_f.color(color)
            turtle_f.goto(points[f'pm{i}'])
            turtle_f.pendown()
            turtle_f.goto(points[f'pm{j}'])
            turtle_f.penup()

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


coordinates_for_lines = list(zip(list_of_points.values(), list(list_of_middles.values())[::-1]))
draw_lines(zolwik, "black", coordinates_for_lines)


zolwik.goto((0,0))
list_of_points = {}
for i in range(1, len(list_of_middles.keys())+1):
    list_of_points[f'p{i}'] = list_of_middles[f'pm{i}']


new_middles = calculate_middles(list_of_points)
draw_points(zolwik, "red", 5, new_middles, 'pm')


draw_sides(zolwik, "green", new_middles)


zolwik.goto(0,0)


turtle.Screen().exitonclick()