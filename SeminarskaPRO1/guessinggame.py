zapis = []
while True:  #Vsa ugibanja in odgovore shranimo v tebelo v parih
             #vhodni podatek 0 zaključi zanko
    stevilo = int(input())
    if stevilo == 0:
        break
    odgovor = input()
    zapis.append((stevilo, odgovor))

spodnja_meja, zgornja_meja = (1,10) #interval možnih rešitev

for i,j in zapis:   #Gre skozi tabelo parov in preveri drugi element vsakega para, če je odgovor "too low", 
    if j == "too low":  #se vrednost spodnje meje intervala posodobi, če pa je odgovor "too high" pa vrednost zgornje meje.
        spodnja_meja = max(spodnja_meja, i + 1)   #v primeru posodobitve spodnje meje vedno primerjamo s prejšno vrednostjo in
                                                  #vzamemo max teh dveh vrednosti, pri zgornji pa minimum.
    elif j == "too high":                         #(to prepreči spremembe intervala v primerih ko goljufa)
        zgornja_meja = min(zgornja_meja, i - 1)
        
    else: #ko je odgovor == "right on"
        
        if spodnja_meja <= i <= zgornja_meja:  #če je število v intervalu, Stan verjetno ni goljufal, če pa ni v intervalu pa je
            print("Stan may be honest")
            spodnja_meja, zgornja_meja = (1,10) #ko se ena runda zaključi postavimo interval na prvotno vrednost 
        else:
            print("Stan is dishonest")
            spodnja_meja, zgornja_meja = (1,10) 
    
     
        

    
