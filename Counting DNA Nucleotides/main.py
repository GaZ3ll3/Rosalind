# -*- coding: utf-8 -*-

if __name__ == "__main__":
    fid = open('rosalind_dna.txt','r')
    output = open('main.out','w')
            
    s = fid.readline().strip()
    #read string
    output.write("%d %d %d %d" % (s.count('A'),s.count('C'),s.count('G'),s.count('T')))
        

fid.close()
output.close()


