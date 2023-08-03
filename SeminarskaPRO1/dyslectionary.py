def slovar_za_dislektike():
    "Uredi slovar po abecedi od zadnje crke do prve"
    skupine = []
    skupina = []
    
    try: #loop deluje dokler ne pridemo do konca vhodnih podatkov
        while True:
        
            beseda = input()  #shranimo besede v tabelo "skupina", ko pa vhodni podatki
            if beseda == "":  #vsebujejo samo prazno vrstico shranimo skupino v
                skupine.append(skupina) #tabelo "skupine"
                skupina = []
    
            else:
                skupina.append(beseda)
    
    except EOFError:            #ko "uporabnik" ne poda nobenih vhodnih podatkov
        skupine.append(skupina) #dodamo se zadnjo skupino tabeli in zaključimo zanko
                                #v konzoli sprožimo s ctrl-d ali ctrl-z
    
    
    
    skupine = uredimo(skupine)
    skupine = poravnamo_desno(skupine)
    
    for skupina in skupine: #izpišemo besede, vsako v svoji vrstici
        for beseda in skupina: 
            print(f"{beseda}")
        if skupine[-1] == skupina:
            break
        print("\n",end='') 

def uredimo(skupine):
    "uredi obrnjene besede po abecedi"
    
    for skupina in skupine:
        obratno = []
        for beseda in skupina:       #gremo skozi vse skupine
            fliped = list(beseda)    #besede razdelimo po črkah 
            fliped.reverse()         #obrnemo vrstni red crk,
            fliped = "".join(fliped) #crke združimo nazaj v besedo
            
            obratno.append(fliped)#obrnjeno besedo shranimo v tabelo
        obratno.sort()            #vse obrnjene besede uredimo po abecednem vrstnem redu
        
        for i in range(len(skupina)):    #besede ponovno obrnemo in jih shranimo
            re_fliped = list(obratno[i]) #nazaj v podtabelo "skupina" v urejenem 
            re_fliped.reverse()          #vrstnem redu obrnjenih besed
            re_fliped = "".join(re_fliped)
            skupina[i] = re_fliped
    return skupine
            
def poravnamo_desno(skupine):
    "Poravna besede na desno"
    
    for skupina in skupine:                    #gremo skozi vse skupine, najdemo najdaljšo besedo
        najdaljsa = max(list(map(len,skupina)))#v skupini, dolžine manjših besed
        for beseda in skupina:                 #odštejemo od najdaljše,
            if len(beseda) < najdaljsa:        #z dobljeno razliko "k" dodamo presledek  
                k = najdaljsa - len(beseda)    #k-krat pred besedo in s tem poravnamo na desno
                skupina[skupina.index(beseda)] = " " * k + f"{beseda}"
    
    return skupine


slovar_za_dislektike()
#pomoc https://www.geeksforgeeks.org/handling-eoferror-exception-in-python/