from dna import *
import sys

class FileParser:

	def __init__(self, file: str):
		self.fasta_suffix = ['.fasta','.FASTA','.fa',
				'.fna','.faa','.ffn,']
		self.fastq_suffix = ['.fastq','.FASTQ','.fq']
		self.sequences = self.parse_file(file)
		self.size = len(self.sequences)

	def parse_file(self, file: str) -> dict:
		for suffix in self.fasta_suffix:
			if file.endswith(suffix):
				fasta = self.parse_fasta(file)
				return fasta
		for suffix in self.fastq_suffix:
			if file.endswith(suffix):
				fastq = self.parse_fastq(file)
				return fastq
		return Exception('Incorrect format type, please input .fasta or .fastq')

	def parse_fasta(self, file: str) -> dict:
		fasta_dict = {}
		try:
			fasta_file = open(file, 'r')
		except:
			raise Exception('File not found in working directory')

		counter = -1
		for line in fasta_file:
			if line[0] == '>':
				counter += 1
				name = line[1:].strip()
				fasta_dict[name] = ''
			else:
				fasta_dict[name] += line.rstrip()
		return fasta_dict


	def parse_fastq(self, file: str) -> dict:
		return {}

def main():
	fasta = FileParser('fast.fa')
	print(fasta.sequences.items())

if __name__ == '__main__':
	main()
