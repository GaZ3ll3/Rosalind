# -*- coding: utf-8 -*-

if __name__ == "__main__":
    fid = open('rosalind_revc.txt','r')
    output = open('main.out','w')
            
    s = fid.readline().strip()
    #read string
    sta = s.replace('T','t').replace('t','a').replace('A','T').replace('a','A')
    scg = sta.replace('C','c').replace('c','g').replace('G','C').replace('g','G')
    output.write("%s" %(scg[::-1]))
        

fid.close()
output.close()
