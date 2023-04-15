from turtle import Screen, Turtle
def zmajnica(n,dolzina, kot):
    "Narise zmajnico"
    if n == 0:
        zelva.fd(dolzina)
    else:
        zmajnica(n-1,dolzina, 90)
        zelva.lt(kot)
        zmajnica(n-1,dolzina, -90)
        

    
okno = Screen()
zelva = Turtle()
zelva.speed(0)

zmajnica(14, 5, 90)


okno.exitonclick()
