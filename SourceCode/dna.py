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
    #Complementation and IUPAC tables needed for dna transformations
    #dna parameter returns a boolean whether or not the sequence contains proper nucleotides
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
        self.length = len(self.sequence)
    #Corrects any nucleotides that are not IUPAC coded or any lowercase nucleotides
    #Runs in O(n) where n is the length of the sequence
    #Memory is n^2 where n is the length of the sequence because a new string is created
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
    #Returns sequence if the dna object does not have a name
    def __str__(self) -> str:
        if self.name == None:
            return self.sequence
        return self.name
    
    #Compute the complement of dna object if and only if the sequence is correctly a dna molecule
    #Runs in O(n) where n is the length of the sequence
    #Memory is n^2 where n is the length of the sequence because a new string is created
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
    #Therefore it runs in O(n) where n is the length of the sequence
    def reverse_complement(self) -> str:
        return self.complement()[::-1]
    
    #Compute the transcription of dna object
    #str.replace worst case in this scenario runs in O(n) because of single character searches
    #Memory is O(1) because there is no new sequence created
    def transcription(self) -> str:
        if not self.dna:
            raise Exception('Not valid DNA string. Please correct the sequence.')
        else:
            return self.sequence.replace('T','U')

    
    #TODO: Reduce the time of translation by making caching transcription at initialization?
    #Translates DNA sequence into its corresponding AminoAcid sequence
    #First: Creation of rna sequence is O(n), where n is the length of the sequence
    #Second: For loop checking for codon runs in O(n) because stepping by three indices in string can be ignored in Big O notation
    #Therefore, this method runs in O(n^2)
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
    #Runs in O(n) where n is the length of the sequence being checked
    #Takes no memory as no new sequence is created
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

    #Determine the Hamming Distance between two sequences of the same size
    #Runs in O(n) where n is the length of the two sequences
    #Takes no extra memory as no new sequences are created
    def hamming_dist(self, second_sequence: str) -> int:
        assert isinstance(second_sequence, dna)
        assert self.length == second_sequence.length
        distance = 0

        for index in range(self.length):
            if self.sequence[index] != second_sequence[index]:
                distance += 1
        
        return distance

#TODO: Create editDistance method? Or possible create an editDistance class?
