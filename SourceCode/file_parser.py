""" Create a class FileParser which parsers files based on their suffixes.
    FileParser will parse either a fasta format file or a fastq format file.
    FileParser creates an object which returns a dictionary containing sequence names and sequences

    Parameters:
        file: File path of fasta/fastq to parse. Must contain correct format

    Return:
	dictionary: keys = name, values = sequences
"""
from fastq import *

class FileParser:

	def __init__(self, file: str):
		self.fasta_suffix = ['.fasta','.FASTA','.fa',
				'.fna','.faa','.ffn,']
		self.fastq_suffix = ['.fastq','.FASTQ','.fq']
		self.sequences = self.parse_file(file)
		self.size = len(self.sequences)


	#Function that contains the logic to determine whether to parse FASTA/FASTQ
	#If input file string does not contain the correct file suffix, raise exception
	def parse_file(self, file: str) -> dict:
		for suffix in self.fasta_suffix:
			if file.endswith(suffix):
				fasta = self.parse_fasta(file)
				return fasta
		for suffix in self.fastq_suffix:
			if file.endswith(suffix):
				fastq = self.parse_fastq(file)
				return fastq
		raise Exception('Incorrect format type, please input .fasta or .fastq')


	#TODO: Create tests for parse_fasta
	#Helper function that parses a file in the working directory
	#Returns a dictionary where the name of the sequence is the key and the sequence is the value
	def parse_fasta(self, file: str) -> dict:
		fasta_dict = {}
		try:
			fasta_file = open(file, 'r')
		except:
			raise Exception('File not found in working directory')

		for line in fasta_file:
			if line[0] == '>':
				name = line[1:].strip()
				fasta_dict[name] = ''
			else:
				fasta_dict[name] += line.rstrip()
		fasta_file.close()
		return fasta_dict


	#TODO: FASTQ implementation
	#TODO: Read Up on FASTQ Format and formalize how to deal with quality control
	#Helper function that parses a given file in the working directory
	#Also returns a dictionary, sequence name will still be the key
	#Values of said dictionary still needs to be decided upon due to quality control information
	def parse_fastq(self, file: str) -> fastq_read:
		fastq_dict = {}
		try:
			fastq_file = open(file, 'r')
		except:
			Exception('File not found in directory.')
		return fastq_read(fastq_file)


        """counter = -1
		for line in fastq_file:
			if counter == -1:
				counter += 1
				name = line[1:].strip()
				fastq_dict[name] = ['','']
		     
		return fastq_dict"""


def main():
	fasta = FileParser('fast.fa')
	print(fasta.sequences.items())

if __name__ == '__main__':
	main()
