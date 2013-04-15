# -*- coding: utf-8 -*-
def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))


data_list = []
fout = open('main.out','w')
with open('rosalind_cons.txt') as fp:
    for name, seq in read_fasta(fp):
        data_list.append(seq)
length = len(data_list)
# length of string
L = len(seq)

P = [[0 for x in xrange(L)] for y in xrange(4)] 

Q = ['A','C','G','T']

for x in range(L):
    for y in range(4):
        for z in range(length):
            P[y][x] = P[y][x] + data_list[z][x].count(Q[y])

domi = ""
for x in range(L):
    MAX = 0
    for y in range(4):  
        if P[y][x]>=P[MAX][x]:
            MAX = y       
            #print 'max for ',x, MAX
    if MAX == 0:
        domi = domi+'A'
    elif MAX ==1:
        domi = domi+'C'
    elif MAX ==2:
        domi = domi+'G'
    elif MAX ==3:
        domi = domi+'T'


fout.write('%s\n%s\n%s\n%s\n%s' %(domi,'A: '+str(P[0]).strip('[]').replace(',',''),'C: '+str(P[1]).strip('[]').replace(',',''),'G: '+str(P[2]).strip('[]').replace(',',''),'T: '+str(P[3]).strip('[]').replace(',','')))