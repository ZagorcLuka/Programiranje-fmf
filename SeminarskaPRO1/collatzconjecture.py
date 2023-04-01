pari = []
while True:
    a, b = input().split() #shranimo stevila v tabelo v parih
    if (a, b) == ("0","0"):
        break
    else:
       a, b = map(int, (a,b))
       pari.append((a, b))


def prvo_coll_st(n, obiskani):  
    "zaporedje prvega števila"
    
    stevec = 0             
    while n > 1:           #vsak člen zaporedja shranimo v slovar, kjer število je ključ, vrednost pa indeks
        stevec += 1
        if n % 2 == 0:
            n = int((n / 2))
            obiskani[n] = stevec
        else:
            n = int(((n*3)+1))
            obiskani[n] = stevec
        
        

def drugo_coll_st(n, obiskani):
    "zaporedje drugega števila"
    
    stevec = 0             #za vsak člen drugega števila preverimo če smo ga že srečali v prvem zap.
                           #ce smo, ga vrnemo skupaj z indeksom tega stevila v drugem zap.
    while n >= 1:  #vecje ali enako dodamo če je slučajno drugo stevilo 1    
        if n in obiskani:
            return n, stevec
        stevec += 1
        if n % 2 == 0:
            n = int((n / 2))
        else:
            n = int(((n*3)+1))
       
    

def Collatz(pari):
    "vrne število korakov potrebnih, da se zaporedja srečata"
    
    for i,j in pari:       #gremo skozi pare, pokličemo funkcije za prvo in drugo stevilo
        obiskani = {i: 0}   #stevilo : indeks števila
        prvo_coll_st(i, obiskani)
        n, stevec = drugo_coll_st(j, obiskani) #shranimo iskano število ter indeks
        print(f"{i} needs {obiskani.get(n)} steps, {j} needs {stevec} steps, they meet at {n}")

Collatz(pari)
    
    