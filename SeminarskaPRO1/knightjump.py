import queue #queue tipa FIFO(First in first out), ki deluje po principu prvi noter prvi vn.
#Vrne elemente po istem vrstnem redu, v keterem so bili dodani. Uporabimo ker delati s tabelami je 
#malo počasneje https://www.geeksforgeeks.org/queue-in-python/ 
n = int(input())
sahovnica = []
for i in range(n):  #shranimo nize v "n" parih
    niz = input()
    vrstica = []
    for znak in niz:
        vrstica.append(znak)
    sahovnica.append(vrstica)
    


def BFS_algoritem(sahovnica):
    """BFS algoritem ali Breadth First Search algoritem. Vrne število potez za
    najkrajšo pot do cilja, če cilj ni dosegljiv izpiše -1"""
    for i in sahovnica:
        if "K" in i:                                #Najdemo lokacijo K-ja (zacetni položaj)
            zacetek = sahovnica.index(i), i.index("K")
    cilj = (0,0)
    vrsta = queue.Queue()
    vrsta.put((zacetek,0))                          #vzstavimo v queue začetni položaj in število potez
    obiskano = {zacetek}                            #množica, ki vsebuje že obiskane položaje
    while vrsta.empty() == False:                   #če je queue prazen se zanka zaključi    
        
        polozaj, st_potez = vrsta.get()             #vzamemo prvi element  
        if polozaj == cilj:                         #preverimo če smo na cilju
            return st_potez
        v,s = polozaj                   
        for mv, ms in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]: #možne poteze
            pv, ps = (v+mv,s+ms)  #od našega položaja probamo vse mozne poteze
            
            if 0 <= pv < n and 0 <= ps < n and sahovnica[pv][ps] != "#" and (pv,ps) not in obiskano: 
                vrsta.put(((pv,ps),st_potez+1))     #preverimo če je pravilna poteza(mesto ne vsebuje "#", ni izven "meje",ni bilo že obiskano)
                obiskano.add((pv,ps))               #če je dodamo ta položaj in število opravljenih potez v queue
                                                    #dodamo položaj k že obiskanim 
    return -1          #če nemoremo priti do cilja vrnemo -1
    
print(BFS_algoritem(sahovnica))
#Python Path Finding Tutorial - Breadth First Search Algorithm - https://www.youtube.com/watch?v=hettiSrJjM4 (ideja za kodo)