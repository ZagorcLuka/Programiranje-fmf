#pomoc https://www.geeksforgeeks.org/python-hilbert-curve-using-turtle/
#nevem ce je cist isto
from turtle import Screen, Turtle
def pea_krivulja(n, a, h):
    "nariši peanovo krivuljo stopnje n"
    if n == 0:
        return 
    else:
        zelva.rt(a)
        pea_krivulja(n-1,-a,h)
        zelva.fd(h)
        zelva.lt(a)
        pea_krivulja(n-1,a,h)
        
        zelva.fd(h)
        pea_krivulja(n-1,a,h)
        zelva.lt(a)
        zelva.fd(h)
        pea_krivulja(n-1,-a,h)
        zelva.rt(a)
okno = Screen()
zelva = Turtle()
zelva.penup()
zelva.speed(0)
zelva.goto(-300, 200)
zelva.pendown()
pea_krivulja(6, 90, 10)
okno.exitonclick()
