#1<=dolzina,sirina<=1000
#visina kovancev od 0 do 10**9
import heapq #rabimo heap queue algorithm ali prioritetni vrstni red, kjer je element z najmanjšo vrednostjo vedno v [0].
#ko dodamo ali vzamemo element struktura tabele vstane ista. 

dolzina, sirina = map(int, input().split())  #vzame dolžino in širino sobe
soba = []                                     
for _ in range(dolzina):      #Sprejme višine kupčkov kovancev
    soba.append(list(map(int, input().split())))  

 
def mozni_sosedi(kup):
    """Vrne vse možne sosedne kupe kovancev"""
    x, y = kup 
    sosedi = [(x-1,y), (x+1, y),(x, y-1), (x, y+1)] 
    return [(x,y) for x, y in sosedi if 0 <= x < dolzina and 0 <= y < sirina] #Edini možni sosedi so tisti, ki niso
                                                                              #negativni in ne "skačejo" izven tabele

def dijkstra(soba, dolzina, sirina): 
    
    """Algoritem, ki najde najkrajšo pot med točkami v nekem drevesu s požrešno metodo(v vsaki fazi 
    izbere lokalno najbolj optimalno odločitev -> točko sz najmanjšo 'ceno'). Ker nas zanima samo pot z 
    najmanjšim maksimumom razlik in ne najhitrejša pot, rabimo gledati samo razlike višin"""
    
    zacetek = (0, 0)  
    konec = (dolzina-1, sirina-1)
    prioritetni_red = [(0, zacetek)]           #prioritetni vrstni red(priority queue), ki ima na začetku samo višino lestve in kordinate začetne točke
    obiskano = set()                      #Uporabimo set(), ker hitreje preverja elemente če so bili že obiskani.
    while prioritetni_red:      #zanka deluje dokler tabela "prioritetni_red" ni prazna
        lestev, trenutni_kup = heapq.heappop(prioritetni_red)    #vzame prvi element tabele ter shrani 
        if trenutni_kup in obiskano:                          
            continue                                          #preveri če so kordinate že bile obiskane
        obiskano.add(trenutni_kup)                            #če so preskoči to iteracijo. če niso doda kordinate
        x, y = trenutni_kup                                   #če smo na končni kordinati funkcije vrne višino lestve
        if trenutni_kup == konec:                 
            return lestev
        for sosed in mozni_sosedi(trenutni_kup):   #pomožna funkcija nam poda kordinate, ki jih lahko obiščemo
            x_i, y_i = sosed               #za vsakega soseda se preveri če je razlika višin večja od maksimuma
            lestev_i = max(lestev, (soba[x_i][y_i] - soba[x][y]))   #če ni se trenutni maksimum razlik(lestev) ne spremeni
            heapq.heappush(prioritetni_red, (lestev_i, sosed))
       
print(dijkstra(soba, dolzina, sirina))        

#Pomoč od Chatgpt; Podal je napačni odgovor(poskusil je rešiti z BFS algoritmom) a me je usmeril v pravo smer. 
#Vir ideje kode: Dijkstra's Shortest Path Algorithm | Graph Theory https://www.youtube.com/watch?v=pSqmAO-m7Lk

