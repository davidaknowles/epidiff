def filterIdenticalReads(inputFileName, outputFileName):
	# Filters identical reads from a file with ChIP-seq reads
	inputFile = open(inputFileName)
	outputFile = open(outputFileName, 'w+')
	lastChrom = ""
	lastStart = 0
	lastEnd = 0
	lastStrand = ""
	for line in inputFile:
		# Iterate through the lines with the reads and keep those that have not been seen before
		# ASSUMES THAT READS ARE SORTED BY CHROMOSOME, THEN START, THEN END, THEN STRAND
		lineElements = line.split("\t")
		if lineElements[0].strip() != lastChrom:
			# The chromosome has changed, so record the read
			outputFile.write(line)
			lastChrom = lineElements[0].strip()
			lastStart = int(lineElements[1].strip())
			lastEnd = int(lineElements[2].strip())
			lastStrand = lineElements[5].strip()
		elif int(lineElements[1].strip()) != lastStart:
			# The start has changed, so record the read
			outputFile.write(line)
			lastStart = int(lineElements[1].strip())
			lastEnd = int(lineElements[2].strip())
			lastStrand = lineElements[5].strip()
		elif int(lineElements[2].strip()) != lastEnd:
			# The end has changed, so record the read
			outputFile.write(line)
			lastEnd = int(lineElements[2].strip())
			lastStrand = lineElements[5].strip()
		elif lineElements[5].strip() != lastStrand:
			# The end has changed, so record the read
			outputFile.write(line)
			lastStrand = lineElements[5].strip()
	inputFile.close()
	outputFile.close()

if __name__=="__main__":
    import sys
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]
    filterIdenticalReads(inputFileName, outputFileName)
