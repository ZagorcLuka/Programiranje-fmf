import turtle
import math
def hisa(zelva, stranica):
    "nariše hišo"
    streha = math.sqrt((stranica/2)**2 + (stranica/2)**2)
    zelva.pensize(5)
    zelva.fd(stranica)
    zelva.lt(90)
    zelva.fd(stranica)
    zelva.lt(90)
    zelva.fd(stranica)
    zelva.lt(90)
    zelva.fd(stranica)
    zelva.bk(stranica)
    zelva.lt(135)
    zelva.fd(streha)
    zelva.rt(90)
    zelva.fd(streha)
    turtle.exitonclick() 

hisa(turtle.Turtle(), 100)
    

    
    
