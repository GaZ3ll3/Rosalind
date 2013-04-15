# -*- coding: utf-8 -*-

import re

if __name__ == "__main__":
    fid = open('rosalind_subs.txt','r')
    #fout = open('out.txt','w')
    s = fid.readline().strip()
    t = fid.readline().strip()
    
    pos = 0
    loc = s.find(t,pos)
    while loc!=-1:
        print loc+1,
        pos = loc+1;
        loc = s.find(t,pos)
        
