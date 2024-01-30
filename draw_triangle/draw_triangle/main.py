import turtle
from find_triangle import biggest_triange as bt
from calc_angles import calculate_angles as cang
from calc_area import calculate_area as car

def write(tur, cor, txt):
    tur.penup()
    tur.speed(0.25)
    tur.goto(cor)
    tur.pendown()
    tur.color('black')

    tur.write(txt, align='center', font=("Verdana", 10, "normal"))


def draw_triangle(sides, angles):
    if len(sides) != 3 or len(angles) != 3:
        raise ValueError("The input lists must contain exactly 3 elements each.")

    # Create a turtle screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)

    # Create a turtle object
    triangle_turtle = turtle.Turtle()
    triangle_turtle.speed(0.55)

    h = 0
    points = ['A', 'B', 'C']

    # Draw the triangle
    for side, angle in zip(sides, angles):

        triangle_turtle.dot(15, 'green')
        triangle_turtle.penup()
        triangle_turtle.forward(20)  # Move away from the green dot
        triangle_turtle.pendown()
        triangle_turtle.write(points[h], align='center', font=("Arial", 16, "normal"))
        triangle_turtle.penup()
        triangle_turtle.backward(20)  # Move back to the green dot
        triangle_turtle.pendown()

        if 0 == h:
            triangle_turtle.forward(side)
            triangle_turtle.setheading(angle)
            h += 1
        elif 1 == h:
            triangle_turtle.forward(side)
            triangle_turtle.setheading(0)
            triangle_turtle.setheading(angle)
            h += 1
        else:
            triangle_turtle.forward(side)
            triangle_turtle.setheading(0)

    write(triangle_turtle, (0,400), f"Area of green triangle is equal {car(sides)}.")

    triangle_turtle.penup()
    triangle_turtle.goto(0,0)

    # Close the window on click
    screen.exitonclick()

# Example usage:
# Lengths of sides
s, _ = bt([3,5,1,4,6])
sides = [x * 100 for x in s]

# Measure of angles
angles = cang(sides)

draw_triangle(sides, angles)
