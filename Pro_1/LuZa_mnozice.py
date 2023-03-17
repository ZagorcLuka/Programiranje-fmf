def razdeli_na_pol_V1(mn):
    "Iz množice 'mn' razdeli pol elementov množici 'A' in pol 'B',če je liho elementov gre odvečni v množico 'A'"
    
    A = set()
    B = set() 
    
    for i in mn: #gre skozi elemente v množici mn
        
        if len(B) == len(mn)//2:  #Množica B se polni dokler je število elementov v množici "B" enako polovici števila elementov v množici "mn"("zaokroženo navzdol")
            A.add(i)              #Ko je ta pogoj izpolnjej se napolni množica "A" s preostalimi elementi množice "mn"
        else:
            B.add(i)
    
    return A, B

print(razdeli_na_pol_V1({5,0,2,9,11,4,1,7})) #sodo ele. 
print(razdeli_na_pol_V1({3,34,77,17,11,55,2,}))#liho ele.
print(razdeli_na_pol_V1({1})) #če je samo en element
print(razdeli_na_pol_V1(set())) #če je množica prazna

print("\n==============================\n")

def razdeli_na_pol_V2(mn):
    "Iz množice 'mn' razdeli pol elementov množici 'A' in pol 'B',če je liho elementov gre odvečni v množico 'A'"
    
    A = set()
    B = set()
    
    
    while mn:  #dokler ni množica "mn" prazna
        element = list(mn)[0]   #množico spremenimo v tabelo in vzamemo prvi element
        if len(mn) % 2 == 0:    #ko je število elementov v množici "mn" sodo se element, ki je v "mn" doda v množico "B" ter se odstrani iz množice "mn"
            B.add(element)      #če je pa liho pa gre v množico "A".
            mn.remove(element) 
        else:
            A.add(element)
            mn.remove(element)  #uporabimo remove() in ne discard(), ker bo izbran element vedno v množici
       
    return A, B

print(razdeli_na_pol_V2({5,0,2,9,11,4,1,7})) #sodo ele. 
print(razdeli_na_pol_V2({3,34,77,17,11,55,2,}))#liho ele.
print(razdeli_na_pol_V2({1})) #če je samo en element
print(razdeli_na_pol_V2(set())) #če je množica prazna




        