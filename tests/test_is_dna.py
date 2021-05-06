#! /usr/bin/env python
import unittest
from dna import *

class test_correction(unittest.TestCase):

	def test_empty_string(self):
		empty_sequence = dna('')
		self.assertFalse(empty_sequence.is_dna())
	
	def test_rna_sequence(self):
		rna_sequence = dna('AGCUAGUCA')
		self.assertFalse(rna_sequence.is_dna())
	
	def test_lower_case_sequence(self):
		lower_dna_sequence = dna('agtCGTAG')
		self.assertTrue(lower_dna_sequence.is_dna())

	def test_non_iupac(self):
		non_iupac = dna('AGTCQGTCG')
		self.assertFalse(non_iupac.is_dna())


if __name__ == '__main__':
	unittest.main()
