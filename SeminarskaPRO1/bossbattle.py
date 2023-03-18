#Boss Battle
#1 <= n <= 100
#"Izpise minimalno koliko bomb se mora nabrati za borbo s Bossom v najslapšem primeru"
n = int(input())   

if n == 1 or n == 2: #če je število stebrov samo 1 ali 2 rabimo 1 bombo.
    print(1)         #drugače pa samo odštejemo 2 od število stebrov in dobimo minimalno potrebnih bomb.
else:
    print(n-2)


         