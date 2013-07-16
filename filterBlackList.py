def makeRegionList(regionFileName):
	# Makes a list of regions, where each entry is a tuple with the region's chromosome, start, end
	regionFile = open(regionFileName)
	regionList = []
	for line in regionFile:
		# Iterate through the lines of the region file and add the information from each line to the list of regions
		lineElements = line.split("\t")
		lineTuple = (lineElements[0], int(lineElements[1]), int(lineElements[2].strip()))
		regionList.append(lineTuple)
	regionFile.close()
	return regionList

def filterBlackList(blackListRegions, readsFileName, outputFileName):
	# Filter black-listed regions from reads
	# ASSUMES THAT READS HAVE BEEN SORTED BY CHROMOSOME, THEN START, THEN END
	# ASSUMES THAT THERE IS AT LEAST 1 BLACK-LISTED REGION
	readsFile = open(readsFileName)
	outputFile = open(outputFileName, 'w+')
	currentRegionIndex = 0
	currentRegionChrom = blackListRegions[currentRegionIndex][0]
	currentRegionStart = blackListRegions[currentRegionIndex][1]
	currentRegionEnd = blackListRegions[currentRegionIndex][2]
	for line in readsFile:
		# Iterate through the reads and record only those that do not overlap black-listed regions
		lineElements = line.split()
		if currentRegionIndex >= len(blackListRegions):
			# There are no black-listed regions that overlap with the current region
			outputFile.write(line)
			continue
		while lineElements[0] > currentRegionChrom:
			# Iterate through the black list regions until a region is found that is on the same chromosome as the current read
			if currentRegionIndex >= len(blackListRegions):
				# All black list regions have been checked, so write the current region to the output file
				outputFile.write(line)
				break
			currentRegionIndex = currentRegionIndex + 1
			if currentRegionIndex >= len(blackListRegions):
				# There are no black-listed regions that overlap with the current region
				outputFile.write(line)
				break
			currentRegionChrom = blackListRegions[currentRegionIndex][0]
			currentRegionStart = blackListRegions[currentRegionIndex][1]
			currentRegionEnd = blackListRegions[currentRegionIndex][2]
		while int(lineElements[1]) >= currentRegionEnd:
			# Iterate through the black list regions until a region is found that is not before the current read
			if (currentRegionIndex >= len(blackListRegions)) or (lineElements[0] != currentRegionChrom):
				# All black list regions have been checked or at least all those on the current chromosome have been check, so write the current region to the output file
				outputFile.write(line)
				break
			currentRegionIndex = currentRegionIndex + 1
			if currentRegionIndex >= len(blackListRegions):
				# There are no black-listed regions that overlap with the current region
				outputFile.write(line)
				break
			currentRegionChrom = blackListRegions[currentRegionIndex][0]
			currentRegionStart = blackListRegions[currentRegionIndex][1]
			currentRegionEnd = blackListRegions[currentRegionIndex][2]
		if currentRegionStart > int(lineElements[2]):
			# There is no black list region that overlaps with the current read, so write the read to the output file
			outputFile.write(line)
	readsFile.close()
	outputFile.close()

def filterBlackListLoop(blackListRegions, readsListFileName, outputFileNameSuffix):
	# Filter black-listed regions from multiple files of reads
	readsListFile = open(readsListFileName)
	for line in readsListFile:
		# Iterate through the files with reads and filter out the black list regions for each file
		print "Filtering reads for " + line.strip()
		outputFileName = line.strip() + "." + outputFileNameSuffix
		filterBlackList(blackListRegions, line.strip(), outputFileName)
	readsListFile.close()

if __name__=="__main__":
   import sys
   blackListRegionsFileName = sys.argv[1] 
   readsListFileName = sys.argv[2]
   outputFileNameSuffix = sys.argv[3]
   isLoop = int(sys.argv[4])
   blackListRegions = makeRegionList(blackListRegionsFileName)
   if isLoop == 1:
	# There is a list of files that need to be filtered
   	filterBlackListLoop(blackListRegions, readsListFileName, outputFileNameSuffix)
   else:
	outputFileName = readsListFileName + "." + outputFileNameSuffix
	filterBlackList(blackListRegions, readsListFileName, outputFileName)
