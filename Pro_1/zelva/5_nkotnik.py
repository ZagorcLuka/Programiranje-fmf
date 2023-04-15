import turtle

def nKotnik(zelva, n, d, barva):
    "nariše pravilni n-kotnik z barvo"
    if n < 3 or d < 0:
        return -1 #nevem kako bi vrnil napako, preden se turtle okence odpre
    
    kot = 180 - (((n-2)*180)/n)
    zelva.pensize(5)
    if barva == None:
        pass
    else:
        zelva.fillcolor(barva)
        zelva.begin_fill()
    for i in range(n):
        
        zelva.fd(d)
        zelva.lt(kot)
    zelva.end_fill()   
    turtle.exitonclick()
    
nKotnik(turtle.Turtle(),2,100,"purple")
    
    