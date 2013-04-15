# -*- coding: utf-8 -*-
import numpy
    
if __name__ == "__main__":
    fid = open('rosalind_lia.txt','r')
    #fout = open('out.txt','w')
    k,N = [float(x) for x in fid.readline().split()]
    
    print float(sum(numpy.random.binomial(2**k,0.25,2000000)>=N))/2000000.00
    
 
