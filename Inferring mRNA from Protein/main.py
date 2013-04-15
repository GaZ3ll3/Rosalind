# -*- coding: utf-8 -*-
dict = {'A':4,'R':6,'N':2,'D':2,'C':2,'Q':2,'E':2,'G':4,'H':2,'I':3,'L':6,'K':2,'M':1,'F':2,'P':4,'S':6,'T':4,'W':1,'Y':2,'V':4,'*':3}

if __name__ == "__main__":
    fid = open('rosalind_mrna.txt','r')
    #fout = open('out.txt','w')
    s = fid.readline().strip()
    #Protein
    prod = 1
    for x in range(len(s)):
        prod = prod*dict[s[x]]
        if prod>1000000:
            prod = prod % 1000000
    
    #stop!
    prod = prod*3
    prod = prod % 1000000
    print prod
        

