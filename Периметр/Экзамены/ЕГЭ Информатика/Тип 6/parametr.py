from turtle import *

tracer(0)
screensize(2000, 2000)
m = 30
x = 5

for _ in range(4):
    fd(x*m)
    rt(90)
    fd(x*m)
    lt(90)
    fd(x*m)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*m, y*m)
        dot(3, "blue")
    
for k in range(1000):
    if k*k*4 + (k-1)*(k-1) > 1500:
        print(k)
        break
