import turtle
import math
import random

def vecHis(zelva, n):
    "Nariše n hiš različnih barv in velikosti"
    barve = ["blue","red","pink","black","white","yellow"]
    for i in range(n):
        
        d = random.randint(50,200)
        roof = math.sqrt((d/2)**2 + (d/2)**2)
        fasada = barve[random.randint(0,5)]
        streha = barve[random.randint(0,5)]
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
        
        zelva.penup()
        zelva.lt(random.randint(1,360))
        zelva.fd(random.randint(10,100))
        
        
        zelva.pendown()
        
    turtle.exitonclick()

vecHis(turtle.Turtle(), 10)