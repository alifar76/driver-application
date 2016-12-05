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
    """ Given two reads, find the length of overlap between the two  """
    # Returns a list with one element. The element is the no. of bp with which two read overlap
    candidates_overlaps = [l for l in range(min(len(read1),len(read2))/2, min(len(read1),len(read2))) if read1[-l:] == read2[:l]]
    # If two reads overlap, return the no. of overlapping bps, else return 0
    return max(candidates_overlaps) if len(candidates_overlaps)>0 else 0

def generate_assembly(consensus,remaining_reads):
    while len(remaining_reads)>0:
        # Return length of overlap and overlap read
        overlap_length, best_overlap = max( [(find_overlap(consensus,b), b) for b in remaining_reads], key = lambda x: x[0] )
        #print overlap_length, best_overlap
        if overlap_length == 0:
            break
        remaining_reads.remove(best_overlap)
        consensus += best_overlap[overlap_length:]
    return consensus


if __name__ == '__main__':
    startTime = datetime.now()
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Assemble Reads Script',
    epilog='''
An example to run the script:
python assemble_reads.py -i input_reads.txt -p genome_assmbled.txt
    ''')
    parser.add_argument('-i', metavar='Input file', nargs=1, help='Name of input file with\
                        sequenced reads',required=True)
    parser.add_argument('-o', metavar='Output file' , nargs=1, help='Name \
                            of output file',required=True)
    args = parser.parse_args()
    data = fasta_iter(args.i[0])
    seqs = data.values()
    result = reverse_complement(generate_assembly(reverse_complement(seqs[0]), 
    map(reverse_complement,seqs[1:])))[:-len(seqs[0])] + generate_assembly(seqs[0], seqs[1:])
    outfile = open(args.o[0],'w')
    outfile.write(result)
    outfile.close()
    print "\n"+"Task Completed! Completion time: "+ str(datetime.now()-startTime)




example_in = """
ATTAGACCTG
CCTGCCGGAA
AGACCTGCCG
GCCGGAATAC """
example_out = 'ATTAGACCTGCCGGAATAC'


#s = example_in.split()
#rosalind = reverse_complement(generate_assembly(reverse_complement(s[0]), 
#    map(reverse_complement,s[1:])))[:-len(s[0])] #+ generate_assembly(s[0], s[1:])
#print (rosalind)
#rosalind = generate_assembly(s[0], s[1:])
#print rosalind == example_out


infile = 'rosalind_long.txt'
data = fasta_iter(infile)
seqs = data.values()
rosalind2 = reverse_complement(generate_assembly(reverse_complement(seqs[0]), 
    map(reverse_complement,seqs[1:])))[:-len(seqs[0])] #+ generate_assembly(seqs[0], seqs[1:])
print (rosalind2)
#rosalind3 = generate_assembly(seqs[0],seqs[1:])
"""outfile = open('assembled_genome.txt','w')
outfile.write(rosalind3)
outfile.close()"""


#rosalind = reverse_complement(extend(reverse_complement(s[0]), map(reverse_complement,s[1:])))[:-len(s[0])] + extend(s[0], s[1:])