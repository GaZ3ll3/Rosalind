# -*- coding: utf-8 -*-
import math    
if __name__ == "__main__":
    fid = open('rosalind_prob.txt','r')
    #fout = open('out.txt','w')
    s = fid.readline().strip()
    array = [float(x) for x in fid.readline().split()]
    #print s
    #print array
    cg = s.count('C')+s.count('G')
    at = len(s) - cg
    barray = []
    for x in range(len(array)):
        barray.append(math.log10((array[x]/2)**cg*(.5-array[x]/2)**at))
    
    for x in range(len(array)):
        print barray[x],
    