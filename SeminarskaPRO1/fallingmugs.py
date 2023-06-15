import math


def skodelica():
    "Preveri, če je dano število, možna višina skodelice"
    D = int(input())                                # a**2 - b**2 = D  =>  (a-b)(a+b) = D
    for a_minus_b in range(1, int(math.sqrt(D)+1)): # gremo skozi možne faktorje števila D od 1 do vključno korena št. 
        
        if D % a_minus_b == 0:                  #preverimo če lahko delimo s faktorjem št. D 
            a_plus_b = D // a_minus_b           #izračunamo (a+b)
            if (a_plus_b + a_minus_b) % 2 == 0: #preverimo če sta oba soda ali liha
                a = (a_plus_b + a_minus_b) // 2 #izračunamo a
                b = (a_plus_b - a_minus_b) // 2 #izračunamo b
               
                return f"{b} {a}"
    return "impossible"                         #če nismo našli nobene možne kombinacije izpišemo "impossible"

print(skodelica())
    