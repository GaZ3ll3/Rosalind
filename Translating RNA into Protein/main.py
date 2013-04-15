# -*- coding: utf-8 -*-
bases = ['u', 'c', 'a', 'g']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

def translate(seq):
    seq = seq.lower().replace('\n', '').replace(' ', '')
    #print seq
    peptide = ''
    
    for i in xrange(0, len(seq), 3):
        codon = seq[i: i+3]
        amino_acid = codon_table.get(codon, '*')
        #print amino_acid
        if amino_acid != '*':
            peptide += amino_acid
        else:
            break
                
    return peptide

#print translate('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')

if __name__ == "__main__":
    fid = open('rosalind_prot.txt','r')
    #fid = open('main.txt','r')
    #fout = open('out.txt','w')
    '''
    n = int(fid.readline().strip())
    s = [int(x) for x in fid.readline().split()]
    '''
    s = fid.readline().strip()
    #print s
    print translate(s)
    
     