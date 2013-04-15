# -*- coding: utf-8 -*-
import itertools

def compare(item1, item2):
    global string
    for x in range(min(len(item1),len(item2))):
        if string.find(item1[x])<string.find(item2[x]):
            return -1
        elif string.find(item1[x])>string.find(item2[x]):
            return 1
        else:
            continue
    if len(item1)>len(item2):
        return 1
    elif len(item1)<len(item2):
        return -1
    else:
        return 0
           
if __name__ == "__main__":
    fid = open('rosalind_lexv.txt','r')
    fout = open('out.txt','w')
    string = fid.readline().strip().replace(' ','')
    n = int(fid.readline().strip())
    array = list(string)
    permu_l = []
    for x in range(n):
        permu_l = permu_l+[p for p in itertools.product(array, repeat=x+1)]
    # sort
    
    #print permu_l
    #sorted(permu_l,cmp = compare)
    perm = []
    for x in permu_l:
        y = list(x)
        perm.append(''.join(list(y)))
        #print (''.join(list(y)))
        #fout.write('%s\n' %(''.join(list(y))))
    #sort!
    for x in sorted(perm,cmp=compare):
        fout.write('%s\n' %(x))
    
    

    
    

