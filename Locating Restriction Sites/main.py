import sys
import string

argc = len(sys.argv)
data_file_loc = "rosalind_revp.txt"
usage = """revp.py [data file]
Finds all reverse compliments in a strands of DNA of length 4-8."""
toCompliment = string.maketrans("ACGT", "TGCA")

if argc > 2:
    print(usage)
    sys.exit(1)
if argc == 2:
    data_file_loc = sys.argv[1]

try:
    data_file = open(data_file_loc)
    data_file.readline()
    strand = data_file.read().replace('\n','')
    inv_strand = strand.translate(toCompliment)[::-1]
    data_file.close()
except IOError, error:
    print(error)
    print(usage)
    sys.exit(1)

forward_offsets = [4, 6, 8]
rev_offset_index = 0
index = 0
max_index = len(strand)
pal_positions = []
pal_lengths = []

while index < max_index:
    for offset in forward_offsets:
            if index + offset >= max_index:
                continue
            if(strand[index: index + offset] == 
               inv_strand[max_index - index - offset:max_index - index]):
                pal_positions.append(index + 1)
                pal_lengths.append(offset)
            rev_offset_index -= 1
    index += 1           

for print_index, position in enumerate(pal_positions):
    print("%d %d" %(position, pal_lengths[print_index]))