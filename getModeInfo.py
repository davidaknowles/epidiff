def getModeInfo(fileNameListFileName, modeFileName):
	# Creates a script that sorts files from a list
	fileNameListFile = open(fileNameListFileName)
	modeFile = open(modeFileName, 'w+')
	for line in fileNameListFile:
		# Iterate through lines of the file and make a script that sorts them
		fileNameElements = line.split("_")
		if (fileNameElements[1] == "H3K27me3") or (fileNameElements[1] == "H3K36me3"):
			# Have histone mark for a broad peak
			modeFile.write("Broad")
		else:
			modeFile.write("Narrow")
		modeFile.write("\n")
	fileNameListFile.close()
	modeFile.close()

if __name__=="__main__":
    import sys
    fileNameListFileName = sys.argv[1]
    modeFileName = sys.argv[2]
    getModeInfo(fileNameListFileName, modeFileName)
