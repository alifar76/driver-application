from itertools import groupby
from string import maketrans



def fasta_iter(fasta_name):
    """ Given a fasta file. return dict with header as key, 
    and sequence as value """
    file_dict = {}
    fh = open(fasta_name, 'rU')
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        header = header.next()[1:].strip()		# Drop the ">"
        seq = "".join(s.strip() for s in faiter.next())		# Join all sequence lines to one.
        file_dict[header] = seq
    return file_dict    

def reverse_complement(s):
    return s.translate(maketrans('ACTG','TGAC'))[::-1]

def find_overlap(read1,read2):
    # Returns a list with one element. The element is the no. of bp with which two read overlap
    candidates_overlaps = [l for l in range(min(len(read1),len(read2))/2, min(len(read1),len(read2))) if read1[-l:] == read2[:l]]
    # If two reads overlap, return the no. of overlapping bps, else return 0
    return max(candidates_overlaps) if len(candidates_overlaps)>0 else 0

def extend(consensus,remaining_reads):
    while len(remaining_reads)>0:
        # Return length of overlap and overlap read
        overlap_length, best_overlap = max( [(find_overlap(consensus,b), b) for b in remaining_reads], key = lambda x: x[0] )
        #print overlap_length, best_overlap
        if overlap_length == 0:
            break
        remaining_reads.remove(best_overlap)
        consensus += best_overlap[overlap_length:]
    return consensus





example_in = """
ATTAGACCTG
CCTGCCGGAA
AGACCTGCCG
GCCGGAATAC """
example_out = 'ATTAGACCTGCCGGAATAC'


s = example_in.split()
rosalind2 = extend(s[0], s[1:])
print rosalind2 == example_out



#rosalind = reverse_complement(extend(reverse_complement(s[0]), map(reverse_complement,s[1:])))[:-len(s[0])] + extend(s[0], s[1:])


data = fasta_iter('coding_challenge_data_set.txt')
seqs = data.values()

#testdata = reverse_complement(extend(reverse_complement(seqs[0]), map(reverse_complement,seqs[1:])))[:-len(seqs[0])] + extend(seqs[0], seqs[1:])
#print (testdata)