import queue #queue tipa FIFO(First in first out), ki deluje po principu prvi noter prvi ven

while True: 
    podatki =  input().split(" ")
    if podatki[0] == "0": #zanko zaključimo ko vtipkamo 0 0 0
        break
    
    dungeon = []
    for i in range(int(podatki[0])):
        level = []
        for j in range(int(podatki[1])):#shranimo informacije o nivojih v podtabele
            vrstica = list(input())
            level.append(vrstica)
            if "S" in vrstica: #shranimo začetni položaj
                zacetek = i, j, vrstica.index("S")
        dungeon.append(level)
        presledek = input()
    
    st_potez = 0
    vrsta = queue.Queue()  
    vrsta.put((zacetek,st_potez)) #vstavimo v queue začetni položaj in število potez
    obiskano = {zacetek} #množica, ki vsebuje že obiskane položaje
    
    while vrsta.empty() == False :  #če je queue prazen se zanka zaključi    
        polozaj, st_potez = vrsta.get() #vzamemo prvi element  
        
        l,v,s = polozaj  #l-nivo, v-vrstica, s-stolpec
        if dungeon[l][v][s] == "E": #preverimo ce smo na cilju                      
            print(f"Escaped in {st_potez} minute(s).") 
            break
        
        for ml, mv, ms in [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]: #vse možne poteze
            pl, pv, ps = (l+ml, v+mv, s+ms) #Gremo skozi vse možne poteze od našega trenutnega položaja
            
            if (0<=pl<int(podatki[0]) and 0<=pv<int(podatki[1]) and #ce nas poteza ne vrže izven meje, 
                0<=ps<int(podatki[2]) and dungeon[pl][pv][ps] != "#" and #ne naletimo na "#" in nismo še 
               (pl, pv, ps) not in obiskano):                            #obiskali to mesto, potem dodamo 
                                                                     #nov položaj in št. trenutnih potez
                vrsta.put(((pl,pv,ps),st_potez+1))                   #na konec naše vrste. 
                obiskano.add((pl,pv,ps))                             #položaj še dodamo k obiskanim
        
        if vrsta.empty() == True: #če nobena poteza ni bila pravilna potem labirint ni rešljiv
            print("Trapped!") 
            
            