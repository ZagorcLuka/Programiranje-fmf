import math

n = input()
def fakulteta_n(n):
    "Od razultata n fakultete izračuna število n"
    n_stevke = len(n)
    if n_stevke < 4:      #če je število pod 4 lahko izračunamo kar "na dolgo"  
        x = 1             #izračunamo n fakultete in primerjamo 
        N = 1             #razultate z našim n-jem
        while x < int(n):   
            N += 1
            x *= N
        return N
    else:                 #ko je število večje pa uporabimo lastnost logaritmov in sicer
        N = 0             #log(a*b) = log(a) + log(b). Ker je hitreje seštevati logaritme
        stevke = 1        #kot pa računati n!. Uporabimo logaritem z osnovo 10, od koder 
                          #pridobimo število števk števila (če zaokrožimo navzgor).
        while stevke < n_stevke:  #ko prekoračimo število števk danega števila 
            N += 1                #vrnemo iskano število N od N!
            stevke += math.log(N,10)
            
        return N
        

print(fakulteta_n(n))

#pomoč - https://www.geeksforgeeks.org/count-digits-in-a-factorial-using-logarithm/