from itertools import groupby


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


data = fasta_iter('coding_challenge_data_set.txt')
seqs = data.values()


def find_overlaps(arr, acc=''):
    if len(arr) == 0:
        return acc

    elif len(acc) == 0:
        acc = arr.pop(0)
        return find_overlaps(arr, acc)

    else:

        for i in range(len(arr)):
            a = arr[i]
            l = len(a)

            for p in range(l / 2):
                q = l - p

                if acc.startswith(a[p:]):
                    arr.pop(i)
                    return find_overlaps(arr, a[:p] + acc)

                if acc.endswith(a[:q]):
                    arr.pop(i)
                    return find_overlaps(arr, acc + a[q:])


small_dataset = """
ATTAGACCTG
CCTGCCGGAA
AGACCTGCCG
GCCGGAATAC
"""

example_in = """
ATTAGACCTG
CCTGCCGGAA
AGACCTGCCG
GCCGGAATAC """


example_out = 'ATTAGACCTGCCGGAATAC'


#print small_dataset.split()
#print find_overlaps(small_dataset.split())
#print find_overlaps(seqs)





from string import maketrans
def revcomp(s):
    return s.translate(maketrans('ACTG','TGAC'))[::-1]

def overlap(a,b):
    print a, b
    candidates_overlaps = [l for l in range(min(len(a),len(b))/2, min(len(a),len(b))) if a[-l:] == b[:l]]
    print candidates_overlaps
    return max(candidates_overlaps) if len(candidates_overlaps)>0 else 0

def extend(consensus,remaining_reads):
    while len(remaining_reads)>0:
        overlap_length, best_overlap = max( [(overlap(consensus,b), b) for b in remaining_reads], key = lambda x: x[0] )
        #print overlap_length, best_overlap
        if overlap_length == 0:
            break
        remaining_reads.remove(best_overlap)
        consensus += best_overlap[overlap_length:]
    return consensus


s = example_in.split()
print (s)
rosalind = revcomp(extend(revcomp(s[0]), map(revcomp,s[1:])))[:-len(s[0])] + extend(s[0], s[1:])



print find_overlaps(example_in.split()) == example_out
print rosalind == example_out


