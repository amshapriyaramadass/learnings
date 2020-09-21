if __name__ == '__main__':

    # There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
    # You like all the integers in set  and dislike all the integers in set . Your initial happiness is . 
    # For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. 
    # Otherwise, your happiness does not change. Output your final happiness at the end.


    # input given
    #   3 2
    #   1 5 3
    #   3 1
    #   5 7
    #  Expected output 
    # 1

    n,m = map(int, input().split())
   
        
    # for _ in range(n):
    inputset = set(input().split())
    # print("input set", inputset)

    aset = set(input().split())
    bset = set(input().split())   
    # print(aset,bset, sep ='\n')  
    hcount = 0

    for i in inputset:
        if i in aset:
            hcount += 1
        elif i in bset:
            hcount -= 1  
        else:
            hcount += 0

    
    # hc1 = len(inputset.intersection(aset))
    # hc2 = len(inputset.intersection(bset))

    # hcount = abs(hc1- hc2)
    print(hcount)

     

       