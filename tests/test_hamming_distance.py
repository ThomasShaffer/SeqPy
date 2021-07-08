#! usr/bin/env python
from file_parser import *
import unittest
from dna import *

class test_hamming_distance(unittest.TestCase):

    def test_incorrect_sizes(self):
        dna_size_8 = dna('ACGTCGAG')
        dna_size_9 = dna('ACGTAGACC')
        dna_size_1 = dna('G')
        dna_size_2 = dna('GC')
        self.assertRaises(AssertionError, dna_size_1.hamming_dist, dna_size_2)
        self.assertRaises(AssertionError, dna_size_9.hamming_dist, dna_size_8)
        
    def test_correct_distance(self):
        dna_correct_1 = dna('ACGTGACGTGACGT')
        dna_correct_2 = dna('ACTTGCCGTGTCGT')
        self.assertEqual(dna_correct_1.hamming_dist(dna_correct_2), 3)


    #def test_non_dna(self):
     #   self.assertRaises()


if __name__ == '__main__':
    unittest.main()
