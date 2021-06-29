#! usr/bin/env python
from file_parser import *
import unittest

class test_correction(unittest.TestCase):

    def test_correct_fastq(self):
    
        """ fastq.fq
        
            @FASTQ_Read1
            AGTGATGAGCACACGTGAC
            +Random
            IPQLRQRLQEPRLRQERQL
            @FASTQ_Read2
            TAUTAUTACGUTUGAUGUAGUAGUTUAGUCU
            +RandomAgain
            1#12310Lofalsdfllliifpdaifdpfio


        """

        fastq = FileParser('fastq.fq').sequences
        self.assertTrue(fastq.read_counts == 2)
        self.assertEqual(fastq.reads['FASTQ_Read1'][0], 'AGTGATGAGCACACGTGAC')
        self.assertEqual(fastq.reads['FASTQ_Read2'][1], '1#12310Lofalsdfllliifpdaifdpfio')


    def test_nonmatching_sizes(self):
        
        """ mismatchfastq.fastq

            @FASTQ_Read1
            AGTGATGACACGTGACGT
            +FASTQ_Read1
            ifadfiii--!__!#!!@@#$wqwe!!
        
        """

        self.assertRaises(AssertionError, FileParser, 'mismatchfastq.fastq')



if __name__ == '__main__':
    unittest.main()
