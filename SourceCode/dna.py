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
    
    #initialization requires string sequence and an optional name
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
        self.iupac = ['A','G','C', 'T', 'R', 
                      'Y', 'S', 'W', 'K', 'M',
                      'B', 'D', 'H', 'V', 'N', 
                      'a', 'c', 'g', 't' , 'r', 
                      'y', 's', 'w', 'k', 'm', 
                      'b', 'd', 'h', 'v', 'n',
                      '.', '-']
        self.dna = self.is_dna()
    
    #Corrects any nucleotides that are not IUPAC coded or any lowercase nucleotides
    def correction(self) -> None:
        new_sequence = ''
        for nucleotide in self.sequence:
            if nucleotide not in self.iupac:
                nucleotide = 'N'
                new_sequence += nucleotide
            elif nucleotide.islower():
                nucleotide = nucleotide.upper()
                new_sequence += nucleotide
            else:
                new_sequence += nucleotide
        self.sequence = new_sequence
    
    #Allows for easy reading of dna sequence
    def __str__(self) -> str:
        return self.sequence
    
    #Compute the complement of dna object
    def complement(self) -> str:
        if not self.dna:
            raise Exception('Not valid DNA string. Please correct the sequence.')
        else:
            complement = ''
            for nucleotide in self.sequence:
                if nucleotide.upper() in self.complementation:
                    complement += self.complementation[nucleotide.upper()]
                else:
                    return str(nucleotide) + ' is not a valid nucleotide argument'
        return complement

    #Dependent on the complement method above
    def reverse_complement(self) -> str:
        return self.complement()[::-1]
    
    #Compute the transcription of dna object
    def transcription(self) -> str:
        if not self.dna:
            raise Exception('Not valid DNA string. Please correct the sequence.')
        else:
            return self.sequence.replace('T','U')

    #Dependent on the transcription method above
    def reverse_transcription(self) -> str:
        return self.sequence.replace('U', 'T')
    
    #Translates DNA sequence into its corresponding AminoAcid sequence
    def translation(self) -> str:
        rna = self.transcription()
        if rna[:3] != 'AUG':
            raise Exception('There is no start codon to initate translation')
        protein = ''
        for i in range(0, len(rna), 3):
            codon = rna[i:i+3]
            if codon not in self.amino_acids:
                raise Exception('Missense mutation. Codon: ' + codon + ' does not encode for amino acid')
            amino_acid = self.amino_acids[codon]
            if amino_acid != 'STOP':
                    protein += self.amino_acids[codon]
            else:
                    return protein
        return protein
    
    #Determines whether sequence is DNA or RNA
    def is_dna(self) -> bool:
        if self.sequence == '' or self.sequence == None:
            return False
        for index, nucleotide in enumerate(self.sequence):
            if nucleotide == 'u' or nucleotide == 'U':
                print('First Uracil found at index: ' + str(index + 1) + '. Probably RNA.')
                return False
            elif nucleotide not in self.iupac:
                print('First Non-IUPAC character - ' + nucleotide + ' at index: ' + str(index + 1))
                return False
        return True
