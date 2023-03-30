import turtle
import math
import random

def puscice(z, st):
    "narise 'st' puscic razlicnih barv"
    z = turtle.Turtle()
    z.pensize(5)
    puscica = math.sqrt(25**2 +90**2)
    naprej = 200
    barve = ["purple","orange","green","blue","red","yellow","grey"]
    kot = 20
    
    for i in range(st):
        st1 = random.randint(0,6)
        st2 = random.randint(0,6)
        z.pencolor(barve[st1])
        z.fillcolor(barve[st2])
        z.begin_fill()                    
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
        z.end_fill()
        
        z.penup()
        z.lt(90)
        z.fd(naprej)
        z.pendown()
        naprej += 50
        
    turtle.exitonclick()

puscice(turtle.Turtle(), 6)