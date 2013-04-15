# -*- coding: utf-8 -*-
import itertools

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
        
def permu(n):
    print fac(n)
    array = range(n+1)
    permu_l = list(itertools.permutations(array[1:n+1],2))
    for x in permu_l:
        print (str(list(x)).strip('[]')).replace(',',' ')
    
if __name__ == "__main__":
    fid = open('rosalind_perm.txt','r')
    n = int(fid.readline().strip())
    permu(n)
    

    
    


