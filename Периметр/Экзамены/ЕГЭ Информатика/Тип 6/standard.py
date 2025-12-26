from turtle import *

tracer(0)
screensize(2000, 2000)
m = 30

width(1)
pencolor("green")
for _ in range(4):
    fd(14*m)
    rt(90)

for _ in range(5):
    fd(5*m)
    rt(45)

"""pencolor("red")
for _ in range(3):
    fd(12*m)
    rt(120)
"""

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3, "blue")

done()
