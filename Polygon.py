import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(500,600)
polygon = turtle.Turtle()

num_side = 7
side_length = 100
angle = 360.0 / num_side
for i in range(num_side):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()
