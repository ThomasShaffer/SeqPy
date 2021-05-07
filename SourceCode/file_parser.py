""" Create a class FileParser which parsers files based on their suffixes.
    FileParser will parse either a fasta format file or a fastq format file.
    FileParser creates an object which returns a dictionary containing sequence names and sequences

    Parameters:
        file: File path of fasta/fastq to parse. Must contain correct format

    Return:
	dictionary: keys = name, values = sequences
"""


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

	#TODO: Create tests for parse_fasta
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

	#TODO: FASTQ implementation
	def parse_fastq(self, file: str) -> dict:
		return {}

def main():
	fasta = FileParser('rosalind_gc.fa')
	print(fasta.sequences['Rosalind_1250'])

if __name__ == '__main__':
	main()
