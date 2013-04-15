# -*- coding: utf-8 -*-

if __name__ == "__main__":
    fid = open('rosalind_hamm.txt','r')
    #output = open('main.out','w')
    str1 = fid.readline().strip()
    str2 = fid.readline().strip()
    hamming = 0
    for x in range(len(str1)):
        if str1[x]==str2[x]:
            continue
        else:
            hamming = hamming +1
    print hamming
    

    fid.close()