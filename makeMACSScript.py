def makeMACSScript(fileNameListFileName, path, outpath, ChIPinputFileName, modeFileName, outputFileName):
	# Creates a script that sorts files from a list
	fileNameListFile = open(fileNameListFileName)
	ChIPinputFile = open(ChIPinputFileName)
	modeFile = open(modeFileName)
	outputFile = open(outputFileName, 'w+')
	for line in fileNameListFile:
		# Iterate through lines of the file and make a script that sorts them
		if "Input" in line:
			# The current line is an input file, so do not call peaks
			ChIPinputFile.readline()
			modeFile.readline()
			continue
		fileName = path + line.strip()
		ChIPInputShort = ChIPinputFile.readline().strip()
		ChIPInput = path + ChIPInputShort
		fileNameElements = line.strip().split("_")
		experimentName = fileNameElements[0] + "_" + fileNameElements[1] + "_" + fileNameElements[2][len(fileNameElements[2])-1]
		mode = modeFile.readline().strip()
		# ASSUMES THAT READS ARE 36bp LONG
		if mode == "Broad":
			# Use broad peaks
			outputFile.write("/opt/python/bin/python2.7 /srv/gs1/projects/snyder/yxl/old_home/yxl/src/MACS-2.0.9/bin/macs2 -t " + fileName + " -c " + ChIPInput + " -n " + outpath + experimentName + " -f BED -g 2480996688 -q 1e-4 --broad" + "\n")
		else:
			outputFile.write("/opt/python/bin/python2.7 /srv/gs1/projects/snyder/yxl/old_home/yxl/src/MACS-2.0.9/bin/macs2 -t " + fileName + " -c " + ChIPInput + " -n " + outpath + experimentName + " -f BED -g 2480996688 -q 1e-5" + "\n")
	fileNameListFile.close()
	outputFile.close()

if __name__=="__main__":
    import sys
    fileNameListFileName = sys.argv[1]
    path = sys.argv[2]
    outpath = sys.argv[3]
    ChIPinputFileName = sys.argv[4]
    modeFileName = sys.argv[5]
    outputFileName = sys.argv[6]
    makeMACSScript(fileNameListFileName, path, outpath, ChIPinputFileName, modeFileName, outputFileName)
