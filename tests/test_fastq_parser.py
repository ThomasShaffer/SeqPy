#! usr/bin/env python
from file_parser import *
import unittest

class test_correction(unittest.TestCase):

    def test_correct_fastq(self):
        fastq = FileParser('fastq.fq')
        self.assertTrue(fastq.sequences.read_counts == 2)








if __name__ == '__main__':
    unittest.main()
