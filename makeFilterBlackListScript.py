def makeFilterScript(fileNameListFileName, path, blackListFileName, outputFileName):
	# Creates a script that sorts files from a list
	fileNameListFile = open(fileNameListFileName)
	outputFile = open(outputFileName, 'w+')
	for line in fileNameListFile:
		# Iterate through lines of the file and make a script that sorts them
		fileName = path + line.strip()
		outputFile.write("/opt/python/bin/python2.7 /srv/gs1/projects/snyder/imk1/P01Project/src/filterBlackList.py " + blackListFileName + " " + fileName + " NoBlack 0" + "\n")
	fileNameListFile.close()
	outputFile.close()

if __name__=="__main__":
    import sys
    fileNameListFileName = sys.argv[1]
    path = sys.argv[2]
    blackListFileName = sys.argv[3]
    outputFileName = sys.argv[4]
    makeFilterScript(fileNameListFileName, path, blackListFileName, outputFileName)
