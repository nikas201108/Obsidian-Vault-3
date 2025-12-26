from turtle import *

speed(10000)
screensize(2000, 2000)
m = 67

fillcolor("white")
begin_fill()
for x in range(3):
    fd(13*m)
    rt(120)
end_fill()
up()
canvas = getcanvas()
ch = {}
c = 0
for x in range(-100, 100):
    for y in range(-100, 100):
       s = canvas.find_overlapping(x*m, y*m, x*m, y*m)
       if s:
         try:
            ch[s] += 1
         except:
            ch[s] = 1

up()
tracer(0)
for x in range(-50, 50):
   for y in range(-50, 50):
      goto(x*m, y*m)
      dot(4, "blue")

print(ch)
done()
