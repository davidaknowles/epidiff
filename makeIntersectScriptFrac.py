def makeIntersectScriptFrac(fileNameListFileName, path, outputFileName, numMarks):
	# Create a script that intersects files from a list, which will be used to compute the fraction of overlaps
	fileNameListFile = open(fileNameListFileName)
	outputFile = open(outputFileName, 'w+')
	fileNameList = fileNameListFile.readlines()
	fileNameIndex = 0
	fileNameListMarkArray = []
	for i in range(numMarks):
		# Create an array of file names for each mark
		fileNameListMarkArray.append([])

	while fileNameIndex < len(fileNameList):
		# Iterate through the file names and make a script that intersects the appropriate files
		currentTempFileName = path + fileNameList[fileNameIndex].strip()
		for i in range(numMarks):
			# Iterate through marks and add the file name for each mark to its array
			fileNameListMarkArray[i].append(fileNameList[fileNameIndex])
			fileNameIndex = fileNameIndex + 1

	for fileNameListMark in fileNameListMarkArray:
		# Iterate through marks and intersect the files for each
		for i in range(len(fileNameListMark) - 1):
			# Iterate through the files that will be intersected
			fileNameOne = fileNameListMark[i].strip()
			for j in range(i+1, len(fileNameListMark)):
				# Iterate through the second files in the intersection
				fileNameTwo = fileNameListMark[j].strip()
				intersectedFileName = path + fileNameOne + "_" + fileNameTwo
				outputFile.write("intersectBed -a " + path + fileNameOne + " -b " + path + fileNameTwo + " > " + intersectedFileName)
				outputFile.write("\n")

	fileNameListFile.close()
	outputFile.close()

if __name__=="__main__":
    import sys
    fileNameListFileName = sys.argv[1]
    path = sys.argv[2]
    outputFileName = sys.argv[3]
    numMarks = int(sys.argv[4])
    makeIntersectScriptFrac(fileNameListFileName, path, outputFileName, numMarks)
