#! /usr/bin/env python
import unittest
from dna import *

class test_correction(unittest.TestCase):

	def test_empty_string(self):
		empty_string = dna('')
		self.assertRaises(Exception)

	def test_non_iupac(self):
		non_iupac = dna('AGTCQGTA')
		self.assertRaises(Exception)

	def test_normal(self):
		normal_sequence = dna('AGTAGACGTAGCAGTG')
		self.assertEqual(normal_sequence.transcription(), 'AGUAGACGUAGCAGUG')

	def test_rna(self):
		rna_sequence = dna('AUGACUGAUCU')
		self.assertRaises(Exception)


if __name__ == '__main__':
	unittest.main()
