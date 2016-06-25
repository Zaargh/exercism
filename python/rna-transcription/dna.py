DNA_TO_RNA = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}


def to_rna(strand):
    return ''.join([DNA_TO_RNA[nucleotide] for nucleotide in strand])
