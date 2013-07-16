def makeIntersectScript(fileNameListFileName, path, outputFileName, numSubsamples):
	# Create a script that intersects files from a list
	fileNameListFile = open(fileNameListFileName)
	outputFile = open(outputFileName, 'w+')
	fileNameList = fileNameListFile.readlines()
	fileNameIndex = 0
	while fileNameIndex < len(fileNameList):
		# Iterate through the file names and make a script that intersects the appropriate files
		currentTempFileName = path + fileNameList[fileNameIndex].strip()
		for i in range(numSubsamples - 1):
			# Iterate through peaks from subsamples of the same original file and intersect them
			fileNameIndex = fileNameIndex + 1
			secondFileName = path + fileNameList[fileNameIndex].strip()
			fileNameElements = secondFileName.split("_")
			nextTempFileName = fileNameElements[0] + "_" + fileNameElements[1] + "_IntersectTemp" + str(i)
			if i == numSubsamples - 2:
				# In the last subsample, so write the intersection to a non-temp file
				intersectedFileName = fileNameElements[0] + "_" + fileNameElements[1] + "_Intersected"
				outputFile.write("intersectBed -a " + currentTempFileName + " -b " + secondFileName + " > " + intersectedFileName + "; rm " + currentTempFileName + "\n")
			else:
				outputFile.write("intersectBed -a " + currentTempFileName + " -b " + secondFileName + " > " + nextTempFileName)
				if i > 0:
					# Remove the previous temporary file
					outputFile.write("; rm " + currentTempFileName)
				outputFile.write("; ")
			currentTempFileName = nextTempFileName
		fileNameIndex = fileNameIndex + 1
	fileNameListFile.close()
	outputFile.close()

if __name__=="__main__":
    import sys
    fileNameListFileName = sys.argv[1]
    path = sys.argv[2]
    outputFileName = sys.argv[3]
    numSubsamples = int(sys.argv[4])
    makeIntersectScript(fileNameListFileName, path, outputFileName, numSubsamples)
