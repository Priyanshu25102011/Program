import turtle

screen = turtle.Screen()
screen.bgcolor("black")

square = turtle.Turtle()

square.pencolor("white")
square.pensize(3)
square.speed(1)

num_sides = 4

for _ in range(num_sides):
    square.forward(100)
    square.right(90)

turtle.done()