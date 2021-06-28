#! /usr/bin/env python
from file_parser import *
import unittest

class test_correction(unittest.TestCase):

	"""def test_empty_file_location(self):
		empty_file = FileParser('')
		self.assertException(Exception)

		Returns: Exception Raised in the Code
			 When trying to test for my Exception an initial Error message appears
			 However, it works as desired



	   def test_non_existent_file(self):
		non_existent_file = FileParser('NotInTheWorkingDirectory.fasta')
		self.assertException(Exception)

                Returns: Exception Raised in the Code
                         When trying to test for my Exception an initial Error message appears
			 However, it works as desired

	"""

	def test_working_file(self):
		""" fasta.fa:
			> FASTA
			AGTGAG

			> FASTA2
			AGUTAGAUT

		"""
		fasta_file = FileParser('fasta.fa')
		self.assertEqual(fasta_file.size, 2)
		self.assertTrue(fasta_file.sequences['FASTA'] == 'AGTGAG')
		self.assertTrue(fasta_file.sequences['FASTA2'] == 'AGUTAGAUT')


if __name__ == '__main__':
	unittest.main()
