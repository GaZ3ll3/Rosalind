# -*- coding: utf-8 -*-

    
if __name__ == "__main__":
    fid = open('rosalind_iev.txt','r')
    #fout = open('out.txt','w')
    array = [float(x) for x in fid.readline().split()]
    
    multiplier = [1.0,1.0,1.0,0.75,0.5,0]
    
    exp = 0
    for x in range(6):
        exp = exp + 2* array[x]*multiplier[x]
    print exp