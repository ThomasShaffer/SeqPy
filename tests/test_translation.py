#! /usr/bin/env python
import unittest
from dna import *

class test_correction(unittest.TestCase):

	def test_empty_string(self):
		empty_string = dna('')
		self.assertRaises(Exception)

	def test_rna_string(self):
		rna_string = dna('AGTAGUATG')
		self.assertRaises(Exception)

	def test_dna_string(self):
		dna_string = dna('ATGCTATAA')
		self.assertEqual(dna_string.translation(), 'ML')

	def test_non_start_codon(self):
		dna_string = dna('GCTACGT')
		self.assertRaises(Exception)

if __name__ == '__main__':
	unittest.main()
