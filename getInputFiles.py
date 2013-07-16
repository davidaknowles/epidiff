def getInputFiles(fileNameListFileName, ChIPinputFileName):
	# Creates a script that sorts files from a list
	fileNameListFile = open(fileNameListFileName)
	ChIPinputFile = open(ChIPinputFileName, 'w+')
	for line in fileNameListFile:
		# Iterate through lines of the file and make a script that sorts them
		fileNameElements = line.split("_")
		ChIPInput = fileNameElements[0] + "_" + "Input_Sorted.NoBlack" + "\n"
		ChIPinputFile.write(ChIPInput)
	fileNameListFile.close()
	ChIPinputFile.close()

if __name__=="__main__":
    import sys
    fileNameListFileName = sys.argv[1]
    ChIPinputFileName = sys.argv[2]
    getInputFiles(fileNameListFileName, ChIPinputFileName)
