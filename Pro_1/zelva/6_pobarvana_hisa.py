import turtle
import math

def pobarvanaHisa(zelva, d, fasada, streha):
    "Narise hiso dane velikosti s pobarvano fasado in streho"
    roof = math.sqrt((d/2)**2 + (d/2)**2)
    zelva.pensize(5)
    zelva.fillcolor(fasada)
    
    zelva.begin_fill() 
    zelva.fd(d)
    zelva.lt(90)
    zelva.fd(d)
    zelva.lt(90)
    zelva.fd(d)
    zelva.lt(90)
    zelva.fd(d)
    zelva.bk(d)
    zelva.end_fill()
    
    zelva.fillcolor(streha)
    zelva.lt(135)
    zelva.begin_fill()
    zelva.fd(roof)
    zelva.rt(90)
    zelva.fd(roof)
    zelva.end_fill()
    
    turtle.exitonclick()


pobarvanaHisa(turtle.Turtle(), 200, "pink","red")