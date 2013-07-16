def makeCatPairsScript(fileNameListFileName, path, outputFileName):
	# Creates a script that cats pairs of consecutive files in a list
	fileNameListFile = open(fileNameListFileName)
	outputFile = open(outputFileName, 'w+')
	fileNameList = fileNameListFile.readlines()
	fileNameListFile.close()
	for i in range(len(fileNameList)/2):
		# Iterate through lines of the file and make a script that concatenates them
		firstFileName = path + fileNameList[2*i].strip()
		secondFileName = path + fileNameList[(2*i) + 1].strip()
		fileNameElements = firstFileName.split("_")
		catedFileName = fileNameElements[0] + "_" + fileNameElements[1] + "_Cat"
		outputFile.write("cat " + firstFileName + " " + secondFileName + " > " + catedFileName + "\n")
	outputFile.close()

if __name__=="__main__":
    import sys
    fileNameListFileName = sys.argv[1]
    path = sys.argv[2]
    outputFileName = sys.argv[3]
    makeCatPairsScript(fileNameListFileName, path, outputFileName)
