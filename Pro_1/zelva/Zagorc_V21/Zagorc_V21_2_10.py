from turtle import Screen, Turtle

def koch(n, dolzina):
    "nariše kochovo snežinko stopnje n"
    if n == 0:
        zelva.fd(dolzina)
    else:
        koch(n-1, dolzina)
        zelva.lt(60)
        koch(n-1, dolzina)
        zelva.lt(-120)
        koch(n-1, dolzina)
        zelva.lt(60)
        koch(n-1, dolzina)
        
okno = Screen()
zelva = Turtle()
zelva.speed(0)
zelva.penup()
zelva.goto(-300, 0)
zelva.pendown()
for i in range(3):
    koch(4, 5)
    zelva.lt(-120)

okno.exitonclick()