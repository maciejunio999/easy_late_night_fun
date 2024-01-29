import turtle
from find_triangle import biggest_triange as bt
from calc_angles import calculate_angles as ca

def draw_triangle(sides, angles):
    if len(sides) != 3 or len(angles) != 3:
        raise ValueError("The input lists must contain exactly 3 elements each.")

    # Create a turtle screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)

    # Create a turtle object
    triangle_turtle = turtle.Turtle()
    triangle_turtle.speed(0.75)

    h = 0

    # Draw the triangle
    for side, angle in zip(sides, angles):
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

    # Close the window on click
    screen.exitonclick()

# Example usage:
# Lengths of sides
s, _ = bt([3,5,1,4,6])
sides = [x * 100 for x in s]

# Measure of angles
angles = ca(sides)

draw_triangle(sides, angles)
