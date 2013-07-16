def makeSortScript(fileNameListFileName, path, outputFileName):
	# Creates a script that sorts files from a list
	fileNameListFile = open(fileNameListFileName)
	outputFile = open(outputFileName, 'w+')
	for line in fileNameListFile:
		# Iterate through lines of the file and make a script that sorts them
		fileName = path + line.strip()
		fileNameElements = fileName.split("_")
		sortedFileName = fileNameElements[0] + "_" + fileNameElements[1] + "_Sorted"
		outputFile.write("sort -u -k1,1 -k2,2n -k3,3n -k6,6 " + fileName + " > " + sortedFileName + "\n")
	fileNameListFile.close()
	outputFile.close()

if __name__=="__main__":
    import sys
    fileNameListFileName = sys.argv[1]
    path = sys.argv[2]
    outputFileName = sys.argv[3]
    makeSortScript(fileNameListFileName, path, outputFileName)
