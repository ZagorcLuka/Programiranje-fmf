#2<=N<=100 stevilo delavcev
#1<=L<=U<=2N 2 števili, ki predstavljata preference temperature enega delavca

st_delavcev = int(input())
preference = []

for i in range(st_delavcev): #Vsak delavec poda svoje temperaturne preference
    preferenca = input()
    
    preferenca = preferenca.split()          #interval preference delavca se pretvori v celo število in
    preferenca = list(map(int, preferenca))  #se shrani kot par v tabelo
    preference += [preferenca]
    
st_sob = 0 
preference.sort(key = lambda druga_pref: druga_pref[1])  
#elemente v tabeli razvrstimo od manjše proti večje po drugem podelementom elementa. S pomočjo lambde, ki deluje kot "mini" anonimna funkcija
#in key parameter, ki za vsak element aplicira to funkcijo

max_preferenca = 0 #i, j = min preferenca, max preferenca
for i, j in preference: #preveri če je max preferenca prejšnega delavca manjša od min preference trenutnega delavca
    if max_preferenca < i:  #če je dodamo novo sobo
        st_sob += 1        
        max_preferenca = j
print(st_sob)
    

#15 Vrstica vir kode: https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/




