# -*- coding: utf-8 -*-
if __name__ == "__main__":
    fid = open('rosalind_fibd.txt','r')
    #output = open('main.out','w')
            
    n,k = [int(x) for x in fid.readline().split()]
    #read n and k
    #print n,k
    generation = 1
    a,b = 1,1
    array = []
    for x in range(k-1):
        array.append(0)
    array.append(1)
    
    while (generation<=n-1):
        new = 0
        for x in range(k-1):
            new = new+array[x]
            
        for x in range(k-1):
            array[x] = array[x+1]
        array[k-1] = new
            
        generation = generation+1
        #print a
        
    print sum(array)
    
        

fid.close()