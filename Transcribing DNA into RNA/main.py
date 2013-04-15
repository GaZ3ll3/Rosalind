# -*- coding: utf-8 -*-

if __name__ == "__main__":
    fid = open('rosalind_rna.txt','r')
    output = open('main.out','w')
            
    s = fid.readline().strip()
    #read string
    output.write("%s" % (s.replace('T','U')))
        

fid.close()
output.close()

