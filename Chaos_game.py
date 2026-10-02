from turtle import Turtle, tracer, update
import random
a=Turtle()
b=Turtle()
c=Turtle()
d=Turtle()
a.penup()
b.penup()
c.penup()
d.penup()
a.goto(100, 50)
b.goto(-150, -100)
c.goto(0, 200)
d.goto(150, -100)
b.dot(10)
c.dot(10)
d.dot(10)
tracer(0)
for s in range(10000000000000000000000000):
    t=random.randint(1, 3)
    if t==1:
        a.color("red")
        a.setheading(a.towards(b))
        dis=a.distance(b)

        a.forward(dis/2)

        a.dot(3)
    if t==2:
        a.color("blue")
        a.setheading(a.towards(c))
        ds=a.distance(c)
        a.forward(ds/2)
        a.dot(3)

    if t==3:
        a.color("green")
        a.setheading(a.towards(d))

        di=a.distance(d)

        a.forward(di/2)

        a.dot(3)

    if s%100 == 0:
        update()
input()