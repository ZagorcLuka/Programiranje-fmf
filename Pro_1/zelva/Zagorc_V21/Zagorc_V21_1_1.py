from turtle import Turtle, Screen

def stranica(zelva, n, dolzina):
    "Nariše kvadrat z izboklinami reda n in vrne dolzino crt in ploscino"
    
    if n == 1:
        zelva.fd(dolzina)
        return dolzina, 0
    else:
       zelva.fd(dolzina/3)
       zelva.lt(90)
       zelva.fd(dolzina/3)
       zelva.rt(90)
       
       obseg_rek, ploscina_rek = stranica(zelva, n-1, dolzina/3)
       
       zelva.rt(90)
       zelva.fd(dolzina/3)
       zelva.lt(90)
       zelva.fd(dolzina/3)
       obseg = 4* dolzina / 3 + obseg_rek
       ploscina = (dolzina / 3) ** 2 + ploscina_rek
       return obseg, ploscina
       
       
def narisi_kvadrat(zelva, n, dolzina):
    "nariše kvadrat s stranicami stopnje n"
    obseg = 0
    ploscina = dolzina ** 2
    for i in range(4):
        obseg_str, ploscina_str = stranica(zelva, n, dolzina)
        zelva.rt(90)
        obseg += obseg_str
        ploscina += ploscina_str
    return obseg, ploscina


okno = Screen()
zelva = Turtle()
zelva.speed(0)
zelva.pu()
zelva.goto(-100,100)
zelva.pd()
obseg, ploscina = narisi_kvadrat(zelva, 5, 200)
print(f"Obseg lika je {obseg}, ploscina pa {ploscina}")

okno.exitonclick()    