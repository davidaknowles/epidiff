def makeIntersectEnhancersScript(path, enhancersFileNameListFileName, outputFileName):
	# Make a script that will intersect the enhancers and print the number of lines in each intersection
	enhancersFileNameListFile = open(enhancersFileNameListFileName)
	enhancersFileNameList = enhancersFileNameListFile.readlines()
	enhancersFileNameListFile.close()
	outputFile = open(outputFileName, 'w+')
	for i in range(len(enhancersFileNameList)):
		# Iterate through the enhancer files and get the intersection for each
		fileNameOne = path + enhancersFileNameList[i].strip()
		for j in range(i+1, len(enhancersFileNameList)):
			# Iterate through files for intersection
			fileNameTwo = path + enhancersFileNameList[j].strip()
			outputFile.write("intersectBed -a " + fileNameOne + " -b " + fileNameTwo + " > " + fileNameOne + "_" + enhancersFileNameList[j].strip() + "\n")
			outputFile.write("wc " + fileNameOne + "\n")
			outputFile.write("wc " + fileNameTwo + "\n")
			outputFile.write("wc " + fileNameOne + "_" + enhancersFileNameList[j].strip() + "\n")
	outputFile.close()

if __name__=="__main__":
    import sys
    path = sys.argv[1]
    enhancersFileNameListFileName = sys.argv[2]
    outputFileName = sys.argv[3]
    makeIntersectEnhancersScript(path, enhancersFileNameListFileName, outputFileName)
