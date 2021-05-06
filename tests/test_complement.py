#! /usr/bin/env python
import unittest
from dna import *

class test_correction(unittest.TestCase):

	def test_empty_string(self):
		empty_sequence = dna('')
		self.assertEqual(empty_sequence.complement(), '')
	
	def test_lower_case(self):
		lower_case = dna('agtgtcgatg')
		self.assertEqual(lower_case.complement(), 'TCACAGCTAC')

	def test_non_dna(self):
		non_dna = dna('AGT!Q')
		self.assertFalse(non_dna.sequence[1] == non_dna.complement()[1])



if __name__ == '__main__':
	unittest.main()
