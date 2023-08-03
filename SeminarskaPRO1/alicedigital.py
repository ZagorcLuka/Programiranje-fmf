n = int(input())
info = []
for i in range(n): #shranimo skupino števil in informacijo o
                   #skupini skupaj v pare
    podatki = list(map(int, input().split()))
    stevila = list(map(int, input().split()))
    skupaj = [podatki, stevila]
    info.append(skupaj)

vsote = []
for podatki in info: #gremo skozi vse skupine
    
    
    obvezni_el = podatki[0][1] #minimalni obvezni element
    najvecja, vsota, el =  0, 0, 0 
    
    for st in podatki[1]:      #gremo po vrsti skozi stevila skupine 
        
        if st < obvezni_el:              #Če je št. manjše od obveznega primerjamo vsoto(seštejemo podelemente vsoti)
            najvecja = max(najvecja, vsota + el if vsota else 0)#ter shranimo(če je) in resetiramo trenutno vsoto, vsoto podelementom.
            vsota, el = 0, 0  #V primeru, ko nismo naleteli še na obvezni el. , ne seštejemo skupaj podelemente in vsoto ter  
                              #"preskočimo"(drugi argument v funkciji max() nastavimo na 0) primerjanje vsot
        
        elif st == obvezni_el:                         #Če je el. enak obveznemu, primerjamo vsote ter shranimo največjo
            najvecja = max(najvecja, vsota + el if vsota else 0)#Ko prvic naletimo na obvezni el. v trenutni vsoti
            vsota = obvezni_el + el                    #"preskočimo" ta korak.
            el = 0                                     #Zatem prištejemo obvezni el. in podelemente trenutni vsoti in
                                                       #resetiramo vsoto podelementov
        else:
            el += st             #ce je st. vecje od obveznega, prištejemo k podelementom
                                 
    vsote.append(max(najvecja, vsota + el if vsota else 0)) # primerjamo se zadnjo mozno vsoto in shranimo najvecjo v tabelo 
    
for vsota in vsote: #izpisemo vse vsote
    print(vsota)

  
#pomoc https://github.com/JonSteinn/Kattis-Solutions/blob/master/src/Alice%20in%20the%20Digital%20World/Python%203/main.py