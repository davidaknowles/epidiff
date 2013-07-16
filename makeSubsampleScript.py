def makeSubsampleScript(fileNameListFileName, path, outputFileName, subsampleFrac, numSubsamples):
	# Creates a script that sorts files from a list
	fileNameListFile = open(fileNameListFileName)
	outputFile = open(outputFileName, 'w+')
	for line in fileNameListFile:
		# Iterate through lines of the file and make a script that sorts them
		fileName = path + line.strip()
		fileNameElements = fileName.split("_")
		for i in range(numSubsamples):
			# Create a new call to the subsampling code for each round of subsampling
			subsampleFileName = fileNameElements[0] + "_" + fileNameElements[1] + "_Subsample" + str(i)
			outputFile.write("/opt/python/bin/python2.7 /srv/gs1/projects/snyder/imk1/P01Project/src/subsampleReads.py " + fileName + " " + str(subsampleFrac) + " " + subsampleFileName + "\n")
	fileNameListFile.close()
	outputFile.close()

if __name__=="__main__":
    import sys
    fileNameListFileName = sys.argv[1]
    path = sys.argv[2]
    outputFileName = sys.argv[3]
    subsampleFrac = float(sys.argv[4])
    numSubsamples = int(sys.argv[5])
    makeSubsampleScript(fileNameListFileName, path, outputFileName, subsampleFrac, numSubsamples)
