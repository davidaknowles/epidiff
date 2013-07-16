def subsampleReads(inputFileName, subsampleFrac, outputFileName):
	# Subsamples a fraction of the reads with replacement and writes the sampled reads to the output file
	inputFile = open(inputFileName)
	reads = inputFile.readlines()
	numSampledReads = int(round(subsampleFrac * len(reads)))
	outputFile = open(outputFileName, 'w+')
	inputFile.close()
	random.setstate(random.getstate())
	for i in range(numSampledReads):
		# Sample the proper number of reads and write each read to a file
		randLine = random.randint(0, len(reads) - 1)
		outputFile.write(reads[randLine])
	outputFile.close()

if __name__=="__main__":
    import sys
    import random
    inputFileName = sys.argv[1]
    subsampleFrac = float(sys.argv[2])
    outputFileName = sys.argv[3]
    subsampleReads(inputFileName, subsampleFrac, outputFileName)
