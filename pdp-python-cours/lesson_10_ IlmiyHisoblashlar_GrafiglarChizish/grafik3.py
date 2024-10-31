# from turtle import *
# from colorsys import *

# bgcolor ('black')
# tracer(100)
# pensize(4)
# h = 0

# def draw(ang, n):   
#     circle(5+n, 69)
#     left(ang)
#     circle(5+2*n, 60)

# goto(0.0)

# for i in range(500):
#     c = hsv_to_rgb(h, 1, 1)
#     h += 0.005
#     color(c)
#     up()
#     draw(90, i)
#     draw(180, i)
#     down()
#     draw(1/2, i-i)
#     draw(180, i/2)
#     draw(120, i-2)
# from turtle import *
# from time import sleep

# bgcolor ('black')

# t = [Turtle(), Turtle()]
# x=6
# colors = ['red','yellow',]
from time import sleep
from  turtle import *

bgcolor("black")
t = [Turtle(), Turtle()]
x =6
colors = ['green','red','blue','lime']
for index, i in enumerate(t):
    i.speed(0)
    i.color("white")
    i.shape("circle")
    i.shapesize(0.3)
    i.width(3)
    i.pu()
    i.seth(90)
    i.fd(350)
    i.seth(-180)
    i.pd()
t[0].pu()
delay(0)
speed(0)
ht()
sleep(4)

for i in colors:
    color(i)
    for i in range(360):
        t[0].fd(x)
        t[0].lt(1)
        pu()
        goto(t[0].pos())
        pd()
        t[1].fd(2*x)
        t[1].lt(2)
        goto(t[1].pos())
done()
