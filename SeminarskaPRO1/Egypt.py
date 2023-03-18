import math
trikotniki = []
while True:                #shranimo stranice individualnih trikotnikov v tabelo in 
    stranice = input()     #jih uredimo po velikosti (vhodni podatek "0 0 0" zaključi zanko)
    if stranice == "0 0 0":
        break
    stranice = stranice.split()
    stranice = sorted(list(map(int,stranice)))
    trikotniki.append(stranice)
    

for trikotnik in trikotniki:  
    if trikotnik[2] == math.sqrt((trikotnik[0]**2 + trikotnik[1]**2)):
        print("right")      #Za vsak trikotnik preverimo, če je pravokoten tako, da 
    else:                   #izračunamo dolžino hipotenuze s pitagorovim izrekom in
        print("wrong")      #če je izračun enak dani hipotenuzi je trikotnik pravokoten