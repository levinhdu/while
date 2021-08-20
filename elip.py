import turtle
import random
pen = turtle.Turtle()
color = ["red","yellow","brown","blue","skyblue","violet","green"]
pen.pensize(3)
i= 0
# for i in range(36):
#     pen.color(random.choice(color))
#     pen.rt(10)
#     for j in range(2):
#         pen.circle(90, 90)
#         pen.circle(45, 90)
def elip():
    a=0
    while a<2:
        pen.circle(90, 90)
        pen.circle(45, 90)
        a += 1
while i<12:
    pen.color(random.choice(color))
    pen.rt(30)
    elip()
    i += 1

turtle.done()