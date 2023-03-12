#(0<=a,b,c<=10,1<=n<=20)

naloge = input().split()         #Vneseni podatki se ločijo v individualne elemente in se shranijo v tabelo
naloge = list(map(int, naloge))  #Podatki se pretvorijo iz niza v celo števila ter se shranijo nazaj v tabelo.
                                 

if naloge[3] <= sum(naloge[:3]) and naloge[3] >= 3 and 0 not in naloge:
    print("YES")
else:                                            #Če je vsota nalog večja ali enaka številu zahtevanih nalog,
    print("NO")                                  #če je število zahtevanih nalog več kot 3 in
                                                 #če tabela ne vsebuje ničle, se izpiše "YES" drugače pa "NO" 
    
                                      
    
     

   
        



