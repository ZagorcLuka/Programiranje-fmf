from turtle import Screen, Turtle
def lomljenka(zelva, n, d, r):
    "Narise lomljenko stopnje n z dolzino strance d in razmerjem r."
    vsota = 0
    if n > 0:
        zelva.fd(d/2)
        zelva.lt(90)
        vsota += lomljenka(zelva,n-1,d*r/100,r)
        zelva.lt(90)
        vsota += d
        zelva.fd(d)
        zelva.lt(90)
        vsota += lomljenka(zelva,n-1,d*r/100,r)
        zelva.lt(90)
        zelva.fd(d/2)
        
    return vsota
  
okno = Screen()
zelva = Turtle()
zelva.speed(0)
vsota = lomljenka(zelva, 4, 100, 80)
print(f"vsota stranic je : {vsota}")


okno.exitonclick()