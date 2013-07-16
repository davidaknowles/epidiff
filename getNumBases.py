def getNumBases(inputFileName):
	# Gets the number of bases in a bed file
	# ASSUMES THAT NONE OF THE REGIONS IN THE BED FILE OVERLAP WITH EACH OTHER
	inputFile = open(inputFileName)
	numBasesTotal = 0
	for line in inputFile:
		# Iterate through the lines of the file and get the number of bases in the region in each line
		lineElements = line.split("\t")
		start = int(lineElements[1])
		end = int(lineElements[2])
		numBasesLine = end - start + 1
		numBasesTotal = numBasesTotal + numBasesLine
	inputFile.close()
	return numBasesTotal

def getNumBasesLoop(inputFileNameListFileName, outputFileName):
	# Iterates through a list of files and gets the number of bases in each
	inputFileNameListFile = open(inputFileNameListFileName)
	outputFile = open(outputFileName, 'w+')
	for line in inputFileNameListFile:
		# Iterate through the file names and find the number of bases in each file
		print line
		numBasesTotal = getNumBases(line.strip())
		outputFile.write(str(numBasesTotal))
		outputFile.write("\n")
	inputFileNameListFile.close()
	outputFile.close()

if __name__=="__main__":
	import sys
	inputFileNameListFileName = sys.argv[1]
	outputFileName = sys.argv[2]
	getNumBasesLoop(inputFileNameListFileName, outputFileName)
