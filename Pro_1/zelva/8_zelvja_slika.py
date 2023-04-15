#spirala ?
import turtle

z = turtle.Turtle()
z.speed(100)
z.pensize(2)
z.pencolor("purple")
dolz = 10
for i in range(30):
    z.fd(dolz)
    z.lt(45)
    dolz += 10
z.fd(5)  
z.lt(135)
for i in range(30):
    z.fd(dolz)
    z.rt(45)
    dolz -= 10
z.rt(180)
z.fd(5)
z.lt(45)
for i in range(30):
    z.fd(dolz)
    z.lt(45)
    dolz += 10
z.fd(5)
z.lt(135)
for i in range(30):
    z.fd(dolz)
    z.rt(45)
    dolz -= 10

    

turtle.exitonclick()
