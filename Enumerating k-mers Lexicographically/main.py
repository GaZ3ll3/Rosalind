# -*- coding: utf-8 -*-
import itertools

def permu(s,n):
    #print fac(n)
    array = list(s)
    array[0:0]=' '
    permu_l = [p for p in itertools.product(array, repeat=n)]
    for x in permu_l:
        print ''.join(list(x))
    
if __name__ == "__main__":
    fid = open('main.txt','r')
    s = fid.readline().strip().replace(' ','')
    n = int(fid.readline().strip())
    permu(s,n)
    

    
    


