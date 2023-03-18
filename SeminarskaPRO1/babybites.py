#n*(1<=n<=1000) število besed
#ai(0<=ai<=10000) število znakov

st_grizljajev = int(input()) 
besede = input().split()  #To kar dojenček izgovori se shrani v tabelo 

nase_stetje = 1

for i in range(st_grizljajev):  #Preveri ali dojenček pravilno šteje. Tako, da primerja dojenčkovo štetje s našim
                          # štetjem. "mumble" obravnavamo kot pravilno štetje. 
    if str(nase_stetje) == besede[i] or besede[i] == "mumble":  
        nase_stetje += 1
           
    else:
        print("something is fishy")
        break
    if nase_stetje > st_grizljajev:    #Če naše štetje preseže št_grižlajev je bilo dojenčkovo štetje smiselno
        print("makes sense")
        break
        
        

