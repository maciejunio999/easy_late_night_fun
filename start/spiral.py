import turtle

turtle.setup(800, 600)
wn = turtle.Screen()

zolwik = turtle.Turtle()
zolwik.color("blue")
zolwik.penup()      
          
size = 10
for i in range(35):
  zolwik.dot()                
  size = size + 2             
  zolwik.forward(size)          
  zolwik.right(24)

turtle.Screen().exitonclick()