
print("Prva naloga:\n")

def potrebno_narociti(zaloga):
    "Preveri zalogo in vrne manjkajoče izdelke"
    manjkajoci_izdelki = set()  
    if len(zaloga) == 0:              #če je slovar prazen vrnemo prazno množico
        return manjkajoci_izdelki
    
    for izdelek, kolicina in zaloga.items():  #gremo skozi slovar po ključih in vrednostih in 
        if kolicina == 0:                     #shranimo vse izdelke z vrednostjo 0 v množico
            manjkajoci_izdelki.add(izdelek)

    return manjkajoci_izdelki

# Testni primeri:

# Test 1: spodnji izraz mora vrniti {"krompir"}
print(potrebno_narociti({"krompir": 0}))

# Test 2: spodnji izraz mora vrniti prazno množico
print(potrebno_narociti({}))

# Test 3: spodnji izraz mora vrniti vse izdelke
print(potrebno_narociti({"krompir": 0,"banane": 0,"čebula": 0,"čips": 0,"cockta": 0,"cokolada": 0}))

# Test 4: spodnji izraz mora vrniti prazno množico
print(potrebno_narociti({"krompir": 3,"banane": 1,"čebula": 1,"čips": 7,"cockta": 5,"cokolada": 2}))

# Test 5: spodnji izraz mora vrniti {"banane", "cockta", "cokolada"}
print(potrebno_narociti({"krompir": 1,"banane": 0,"čebula": 3,"čips": 6,"cockta": 0,"cokolada": 0}))

print("\n======================================")



print("Druga naloga:\n") 

def zadostna_zaloga(zaloga, nakup):
    "Vrne true če je nakup mogoč oz. če ima trgovina zadostno količino izdelkov v zalogi sicer pa false"
    if len(zaloga) == 0 or len(nakup) == 0: #preverimo če je kkšn slovar prazen 
        return False
    
    mozni_nakupi = set()
    for izdelek, kolicina in nakup.items():                          #gre skozi nakup in prvo preveri če je izdelek v zalogi 
        if izdelek in zaloga and kolicina[0] <= zaloga.get(izdelek): #ter če je količina zadostna.
            continue                                                 #Če sta pogoja izpoljena za vsak izdelek vrnemo True
        else:                                                        #drugače pa False
            return False
    return True 


# Testni primeri:

# Test 1: spodnji izraz mora vrniti False
print(zadostna_zaloga({"mleko": 1}, {"krompir": (5, 2)}))

# Test 2: spodnji izraz mora vrniti False
print(zadostna_zaloga({}, {"krompir": (5, 2)}))

# Test 3: spodnji izraz mora vrniti False
print(zadostna_zaloga({"mleko": 1}, {}))

# Test 4: spodnji izraz mora vrniti False
print(zadostna_zaloga({"mleko": 0,"krompir": 0, "cokolada": 0, "čebula": 0}, {"krompir": (1, 2), "mleko": (3,1)}))

# Test 5: spodnji izraz mora vrniti False
print(zadostna_zaloga({"krompir": 4, "cokolada": 3,}, {"krompir": (5, 2), "cokolada": (3,2)}))

# Test 5: spodnji izraz mora vrniti True
print(zadostna_zaloga({"krompir": 5, "cokolada": 3,}, {"krompir": (5, 2), "cokolada": (3,2)}))


print("\n======================================")


print("Tretja naloga:\n")


def prodaj(zaloga, nakup):
    "Vrne skupno ceno nakupa in posodobi zalogo glede na dani nakup"
    if zadostna_zaloga(zaloga, nakup) == False : #preveri če je zaloga zadostna za nakup
        return None
    
    skupna_cena = 0 
    for izdelek, kolicina in nakup.items():              #gremo skozi nakup, pogledamo ceno izdelka in jo pomnožimo s količino
        skupna_cena += kolicina[1] * kolicina[0]         #ter seštejemo z ostalimi izdelki.
        posodobitev = zaloga.get(izdelek) - kolicina[0]  #Hkrati pa posodabljamo zalogo tako, da odštevamo količine kupljenih
        zaloga.update({izdelek: posodobitev})            #izdelkov z našo zalogo
    return f"Skupna cena: {skupna_cena}, Posodobljena zaloga: {zaloga}"

# Testni primeri:

# Test 1: spodnji izraz mora vrniti: Skupna cena: 40, Posodobljena zaloga: {'krompir': 1, 'špinača': 6, 'mleko': 9}
print(prodaj({"krompir": 1, "špinača": 11, "mleko": 19}, {"špinača": (5, 2), "mleko": (10, 3)})) 

# Test 2: spodnji izraz mora vrniti: none
print(prodaj({"krompir": 1, "špinača": 6, "mleko": 9}, {"špinača": (5, 2), "mleko": (10, 3)})) 

# Test 3: spodnji izraz mora vrniti: Skupna cena: 0, Posodobljena zaloga: {'krompir': 1, 'špinača': 4, 'mleko': 10}
print(prodaj({"krompir": 1, "špinača":4, "mleko": 10}, {"špinača": (0, 2), "mleko": (0, 3)}))

# Test 4: spodnji izraz mora vrniti: Skupna cena: 102, Posodobljena zaloga: {'krompir': 18, 'špinača': 6, 'mleko': 7, 'čebula': 2}
print(prodaj({"krompir": 40, "špinača": 11, "mleko": 20, "čebula": 5}, {"krompir": (22,2), "špinača": (5, 2), "mleko": (13, 3),  "čebula": (3,3)}))

# Test 5: spodnji izraz mora vrniti: Skupna cena: 22717, Posodobljena zaloga: {'krompir': 639, 'špinača': 3815, 'mleko': 4828, 'čebula': 5871, 'cockta': 4959, 'čokolada': 0}
print(prodaj({"krompir": 5032, "špinača": 3820, "mleko": 4838, "čebula": 10000, "cockta": 5193, "čokolada": 1}, 
     {"krompir": (4393,2), "špinača": (5, 2), "mleko": (10, 3), "čebula": (4129, 3), "cockta": (234, 6), "čokolada": (1, 100)}))


