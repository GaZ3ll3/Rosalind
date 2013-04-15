#!/usr/bin/env python

import sys
from StringIO import StringIO
from Bio import Phylo
import re

def nwck(tree,taxa):
  taxa = taxa.split()
  tokens = iter(re.split('([(),])', tree))
  while next(tokens) not in taxa:
    pass
  climbs = 0
  descents = 0
  for token in tokens:
    print token
    if token in taxa:
      break
    if token in ',)':
      if descents > 0:
        descents -= 1
      else:
        climbs += 1
    if token in ',(':
      descents += 1
  #print climbs + descents


if __name__ == '__main__':
    fid = open('rosalind_nwck.txt','r')
    pairs = [l2.split('\n') for l2 in fid.read().strip().split('\n\n')]
    for s, line2 in pairs:
        
        x, y = line2.split()
        tree = Phylo.read(StringIO(s), 'newick')
        sys.stdout.write('%s ' % int(tree.distance(x, y)))
        
        nwck(s,line2)
    sys.stdout.write('\n')


    
