
def hot_hike():
    n = int(input())
    temp = input().split()  
    temp = list(map(int,temp)) #shranimo temperature v tabelo 

    maks = float('inf')
    dan_odhoda = 0
    
    for i in range(n-2):  #gremo po vrsti skozi tabelo temp. 
        M = max(temp[i], temp[i+2]) #vzamemo maksimum temp. i-tega
                            #dneva in i-tega+2
        if M < maks:  #primerjamo maksimum temp. z maksimumom temp. prejšnega možnega odhoda         
            maks = M    #če je manjši imamo novi najmanjši maksimum temp. in novi dan odhoda
            dan_odhoda = i+1
    
    return f"{dan_odhoda} {maks}"

print(hot_hike())