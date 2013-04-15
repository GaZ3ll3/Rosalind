# -*- coding: utf-8 -*-

if __name__ == "__main__":
    fid = open('rosalind_fib.txt','r')
    #output = open('main.out','w')
            
    n,k = [int(x) for x in fid.readline().split()]
    #read n and k
    #print n,k
    generation = 1
    a,b = 1,1
    while (generation<=n-2):
        a,b = a+k*b,a
        generation = generation+1
        #print a
        
    print a
        

fid.close()
#output.close()