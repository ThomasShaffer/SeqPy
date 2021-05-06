#! /usr/bin/env python
import unittest
from dna import *

class test_correction(unittest.TestCase):

	def test_empty_string(self):
		empty_sequence = dna('')
		self.assertRaises(Exception)
	
	def test_lower_case(self):
		lower_case = dna('agtgtcgatg')
		self.assertEqual(lower_case.complement(), 'TCACAGCTAC')

	def test_non_dna(self):
		non_dna = dna('AGT!Q')
		self.assertRaises(Exception)

	def test_normal_string(self):
		normal_dna = dna('AGTCAGTAGAC')
		self.assertEqual(normal_dna.complement(), 'TCAGTCATCTG')

if __name__ == '__main__':
	unittest.main()
