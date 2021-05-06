#! /usr/bin/env python
import unittest
from dna import *

class test_correction(unittest.TestCase):
    
    def test_empty_string(self):
        empty_dna = dna('')
        self.assertEqual(empty_dna.sequence, '')
        empty_dna.correction()
        self.assertEqual(empty_dna.sequence, '')
        
    def test_special_characters(self):
        special_dna = dna('AGTC!*!')
        self.assertEqual(special_dna.sequence, 'AGTC!*!')
        special_dna.correction()
        self.assertEqual(special_dna.sequence, 'AGTCNNN')

    def test_lower_case(self):
        lower_case_dna = dna('agtcagtc')
        self.assertEqual(lower_case_dna.sequence, 'agtcagtc')
        lower_case_dna.correction()
        self.assertEqual(lower_case_dna.sequence, 'AGTCAGTC')

    def test_combination(self):
        combination_dna = dna('aG!Tc-.H~')
        self.assertEqual(combination_dna.sequence, 'aG!Tc-.H~')
        combination_dna.correction()
        self.assertEqual(combination_dna.sequence, 'AGNTC-.HN')

if __name__ == '__main__':
    unittest.main()
