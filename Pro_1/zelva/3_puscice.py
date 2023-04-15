import turtle
import math
def puscice(z, st):
    "narise 'st' puscic"
    z = turtle.Turtle()
    z.pensize(5)
    puscica = math.sqrt(25**2 +90**2)
    naprej = 200
    for i in range(st):
        z.fd(50)
        z.lt(90)
        z.fd(100)
        z.rt(90)
        z.fd(40)
        z.lt(135)
        z.fd(puscica)
        z.lt(90)
        z.fd(puscica)
        z.lt(135)
        z.fd(40)
        z.rt(90)
        z.fd(100)
        z.lt(90)
        z.penup()
        z.fd(200)

        z.lt(90)
        z.fd(naprej)
        z.pendown()
        naprej += 50
    turtle.exitonclick()

puscice(turtle.Turtle(), 3)




