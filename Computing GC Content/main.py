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


mp = 0.0
#max_percentage
with open('rosalind_gc.txt') as fp:
    for name, seq in read_fasta(fp):
        per = float(seq.count('C')+seq.count('G'))*100/float(len(seq))
        if mp<per:
            mp = per
            print name
            print per
        else:
            continue

            
#        print(name, seq)