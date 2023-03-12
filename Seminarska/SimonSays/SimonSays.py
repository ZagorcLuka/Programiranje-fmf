#1<=T<=20 #število poskusov.
#stavek bo imel od 1 do 1000 znakov vključno presledki

T = int(input())

for i in range(T):  #zanka deluje dokler ne naredimo število danih poskusov.
    stavek = input()  #uporabnik vnese stavek, če sta prvi dve basedi "simon says", izpiše stavek brez prvih 11 znakov.
    if "simon says" in stavek:  
        print(stavek[11:])  
    
#vir celotne kode: https://github.com/KentGrigo/Kattis/blob/master/python/simonsays.py
#Nalogo sem rešil sam, a je bila moja koda nepotrebno dolga.
    

            
