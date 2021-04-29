""" Create a class that represents a sequence of DNA
    
    Function of the class:
        Be able to take in a string of nucleotides and represent a sequence of DNA
        Allowing users to be able to compute some simple variations of said DNA sequence
        and also allow for some more advanced analysis including local/global alignment
    
    Parameters: 
        sequence: String of Nucleotides 
        name (optional): String from fasta or fastq. Not necessary
"""


class dna:
    
    #Simple instantiation requirements, name for fasta/fastq
    def __init__(self, sequence: str, name=None):
        self.sequence = sequence
        self.name = name
        self.complementation = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
        self.amino_acids = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    
    def __str__(self):
        return self.sequence
    
    #Compute the complement of dna object
    def complement(self):
        complement = ''
        for nucleotide in self.sequence:
            complement += self.complementation[nucleotide]
        return complement
    
    def reverse_complement(self):
        return self.complement()[::-1]
    
    #Compute the transcription of dna object
    def transcription(self):
        return self.sequence.replace('T','U')
    
    def translation(self):
        rna = self.transcription()
        protein = ''
        for i in range(0, len(rna), 3):
            codon = rna[i:i+3]
            amino_acid = self.amino_acids[codon]
            if amino_acid != 'STOP':
                    protein += self.amino_acids[codon]
            else:
                    return protein
        return protein
