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
    
    def __init__(self, sequence: str, name=None):
        self.sequence = sequence
        self.name = name
        