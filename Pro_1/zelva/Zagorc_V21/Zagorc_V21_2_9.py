from turtle import Screen, Turtle
def drevo(n):
    "Narise fraktalno drevo "
    if n < 10:
        return
    else:
        zelva.fd(n)
        zelva.lt(30)
        drevo(3*n/4)
        zelva.rt(60)
        drevo(3*n/4)
        zelva.lt(30)
        zelva.bk(n)
    
okno = Screen()
zelva = Turtle()
zelva.speed(0)
drevo(100)

okno.exitonclick()