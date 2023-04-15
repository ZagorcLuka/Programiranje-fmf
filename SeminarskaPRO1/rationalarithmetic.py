import math
st = int(input())
primeri = []


for i in range(st):                #števila pretvorimo v int() in jih shranimo skupaj z operatorjem v tabelo 
    vrstica = input().split()      #operator posebej obravnavamo 
    operacija = vrstica.pop(2)
    vrstica = list(map(int,vrstica))
    vrstica.append(operacija)
    primeri.append(vrstica)
  

for racun in primeri:            #gremo skozi vse primere, preverimo katero operacijo vsebuje in izračunamo
    if racun[4] == "+":          #če sta imenovalca drugačna pri odštevanju ali seštevanju jih kar skupaj pomnožimo 
        if racun[1] != racun[3]: #števca pa z nasprotnima imenovalcema
            n = (racun[0]*racun[3]) + (racun[2]*racun[1])
            d = racun[1] * racun[3]
        else:
            n = racun[0] + racun[2]
            d = racun [1]
    
    if racun[4] == "-":
        if racun[1] != racun[3]:
            n = (racun[0]*racun[3]) - (racun[2]*racun[1])
            d = racun[1] * racun[3]
        else:
            n = racun[0] - racun[2]
            d = racun [1]        
    
    if racun[4] == "*":
        n = racun[0] * racun[2]
        d = racun[1] * racun[3]
         
    if racun[4] ==  "/":
        n = racun[0] * racun[3]
        d = racun[1] * racun[2]
        

    
    while math.gcd(n, d) > 1: #pokrajšamo ulomek
        nsd = math.gcd(n, d)
        n = n // nsd    
        d = d // nsd
    
    if d < 0: #če je imenovalec negativen zamenjamo predznak s števcom
        n = -1 * n  #v primeru, da sta oba negativna se pa znebimo obeh predznakov
        d = -1 * d
        
    print(f"{n} / {d}")
    