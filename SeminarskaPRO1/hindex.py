def H_index():
    "Vrne H-Index raziskovalca"
    n = int(input())
    st_citatov = []
    for i in range(n):   #shranimo informacijo v tabelo
        citati = int(input())
        st_citatov.append(citati)
    
    st_citatov.sort()  #uredimo tabelo po velikosti
    h_index = 0
    
    for stevilo in reversed(st_citatov):  #gremo skozi št. citatov
        if stevilo > h_index:             #v padajočem vrstnem redu
            h_index += 1                  #če je število citatov večje od
        else:                             #trenutnega h_indexa ga povečamo
            return h_index                #za 1
    return h_index  
           
print(H_index())
        