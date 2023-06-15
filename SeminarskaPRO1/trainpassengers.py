def vlak():
    "Preveri če so meritve premikanja potnikov konsistentne"
    
    n = input().split()  #n[0] = kapaciteta, n[1] = št. postaj
    n = list(map(int,n))
    
    postaje = [] 
    for i in range(n[1]): #shranimo skupaj skupek števil v tabelo
        meritve = input().split() #vsako postajo v svoji podtabeli
        meritve = list(map(int,meritve))
        postaje.append(meritve)
    
    if postaje[-1][1] > 0 or postaje[-1][2] > 0: 
         return "impossible"   #prvo preverimo če sta na zadnji postaji
                               #vlak in postaja prazna 
    st_potnikov = 0
    for postaja in postaje: #gremo skozi vse postaje in preverimo:
        if st_potnikov < 0:   #-če kdaj št. potnikov pade pod nič
            return "impossible"  #(sproti posodabljamo št. potnikov na vlaku),
        st_potnikov += postaja[1]  #-če kdaj št. potnikov preseže kapacitete vlaka
        st_potnikov -= postaja[0]  #-in če ima postaja čakajoče potnike, ko vlak ni poln
        if st_potnikov > n[0]:    
            return "impossible"    #Če kakšen pogoj ni izpolnjen, izpišemo "impossible"
        if st_potnikov < n[0] and postaja[2] > 0:
            return "impossible"
    if st_potnikov != 0:  #na koncu še preverimo če je št. potnikov enako nič
        return "impossible"  
    return "possible"  #če so bili vsi pogoji izpolnjeni izpišemo "possible"

print(vlak())