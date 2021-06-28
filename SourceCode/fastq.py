class fastq_reads:

    def __init__(self, open_file):
        self.reads = parse_file(open_file)
        self.read_counts = len(reads)
        

    """
    Parses fastq files according to the common (but not standard)
    4 line fastq file format. 

    Example of the common fastq format:

    @FASTQ_Read1
    AGTAGATAGTACACG
    +FASTQ_Read1
    -!!_--!lllPLLLO

    This will return a dictionary with the key being:
    
    FASTQ_Read1

    and the value of the key will be an array of size 2
    containing the read sequence and the corresponding quality score:
    
    ['AGTAGATAGTACACG','-!!_--!lllPLLLO']

    """
    def parse_file(open_file):
        fastq_reads = {}
        
        #Counter to keep track of where in the 4 line sequence we are at
        #0 is the beginning, 1 is the optional line, 2 is the sequence data, 3 is the quality scores
        counter = 0
        for lines in open_file:

            if counter == 0:
                read_name = lines[1:].rstrip()
                #Reads and their quality data are stored as an array within a dictionary, where the
                #key for the values are the name given in the fastq file
                fastq_reads[read_name] = ['','']
                counter += 1
                continue
             
            if counter == 1:
                fastq_reads[read_name][0] += lines.rstrip()
                counter += 1
                continue


            #Repetitive data is stored in the third line of the fastq format.
            if counter == 2:
                counter += 1
                continue

            if counter == 3:
               assert len(lines.rstrip) == len(fastq_reads[read_name][0]), 'Quality sequence must be same length as Read sequence'
                fastq_reads[read_name][1] += lines.rstrip()
                counter = 0
                continue
        return fastq_reads
