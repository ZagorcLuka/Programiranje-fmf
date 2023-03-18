import queue #rabimo queue tipa FIFO(First in first out), ki deluje po principu prvi noter prvi vn.
#Vrne elemente po istem vrstnem redu, v keterem so bili dodani, sepravi prioriteto ima element,
#ki je bil dodan prvi.

n = int(input())
sahovnica = []
for i in range(n):
    vrstica = input()
    sahovnica.append([*vrstica])#https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
   


def mozni_premiki(v,s):
    "Preveri vse možne poteze od trenutnega mesta"
    mozne_poteze = [(v+2,s+1),(v+2,s-1),(v-2,s+1),(v-2,s-1),(v+1,s+2),(v+1,s-2),(v-1,s+2),(v-1,s-2)]
    return [(v,s) for v,s in mozne_poteze if 0 <= v < n and 0 <= s < n and sahovnica[v][s] != "#"] 
                                                                        

def BFS_algoritem(n):
    """Breath first search algoritem, je algoritem, ki najde najkrajšo pot v nekem drevesu,
       kjer točke v drevesu nimajo 'cene'. Naprej obišče začetno točko potem pa vse možne 'sosede'
       (z zgornjimi omejitvami) in potem 'sosede' teh sosedov itd... dokler ne pridemo do željene točke,
       če pa nemoremo pa izpišemo '-1'.Vemo, da je najkrajša pot, ker gremo po vrstnem redu vseh možnih potez"""
    for i in sahovnica:
        if "K" in i:                                   #Najdemo lokacijo K-ja (zacetni položaj)
            zacetek = sahovnica.index(i), i.index("K")
   
    konec = (0,0)
    obiskano = set()
    vrstni_red = queue.Queue() #naredimo Queue 
    vrstni_red.put(zacetek) #dodamo zacetne "kordinate" v queue
    pot = []
    while vrstni_red:
        pot = vrstni_red.get()
        if konec in pot:
            return len(pot)
        
        print(v, s)
        for poteza in mozni_premiki(v, s):
           if poteza == None:
               return -1
           elif poteza not in obiskano:
               obiskano.add(poteza)
               nova_pot = pot + poteza
               vrstni_red.put(nova_pot)
        
print(BFS_algoritem(n))           
               
            
        
#Python Path Finding Tutorial - Breadth First Search Algorithm - https://www.youtube.com/watch?v=hettiSrJjM4 (ideja za kodo)