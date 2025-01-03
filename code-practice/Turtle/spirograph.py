import turtle as t
import random

spiral = t.Turtle()
t.colormode(255)
spiral.speed(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        spiral.color(random_color())
        spiral.circle(100)
        spiral.setheading(spiral.heading() + size_of_gap)

draw_spirograph(5)



screen = t.Screen()
screen.exitonclick()