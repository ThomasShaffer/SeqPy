#! /usr/bin/env python
import unittest
from dna import *

class test_naive_edit_distance(unittest.TestCase):
    
    def test_empty_string(self):
        sequence_one = dna('AGTG')
        sequence_two = dna('')
        self.assertEqual(len(sequence_one), sequence_one.edit_distance_naive(sequence_two))
	
    def test_incorrect_input(self):
        sequence_one = dna('AGTG')
        sequence_two = dna('!!gU')
        self.assertRaises(Exception)
		

    def test_correct_one(self):
        sequence_one = dna('AGTGC')
        sequence_two = dna('AGTGG')
        self.assertEqual(sequence_one.edit_distance_naive(sequence_two), 1)

if __name__ == '__main__':
    unittest.main()
