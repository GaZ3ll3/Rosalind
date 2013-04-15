# -*- coding: utf-8 -*-

def com(n):
    return float(n*(n-1)/2)
    
if __name__ == "__main__":
    fid = open('main.txt','r')
    #fout = open('out.txt','w')
    k,m,n = [int(x) for x in fid.readline().split()]
    
    print 1-(com(n)+com(m)/4+m*n/2)/com(k+m+n)
 
