import turtle
import random

def draw_star(x, y, color, side):
    turtle.color(color)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for k in range(5):
        turtle.forward(side)
        turtle.right(144)
        turtle.forward(side)
    turtle.end_fill()

def random_length():
    return random.randrange(3, 25)

def random_xy_coord():
    return random.randrange(-450, 450), random.randrange(-400, 400)

turtle.title('STARSSSS')
turtle.bgcolor('black')
turtle.speed('fastest')
colors = ['red', 'orange', 'magenta', 'green', 'blue', 'yellow', 'white', 'teal', 'maroon', 'olive', 'lime', 'aqua', 'navy', 'purple']

stars = 200

for k in range(stars):
    color = random.choice(colors)
    side = random_length()
    x, y  = random_xy_coord()
    draw_star(x, y, color, side)
turtle.done()
