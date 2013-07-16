def getIndividualInteractors(PPIFileName, regulatorsFileName):
	# Find all of the genes that interact with each of the regulators
	regulators = []
	regulatorsFile = open(regulatorsFileName)
	for line in regulatorsFile:
		# Iterate through regulators and put each of them into the regulators array
		regulators.append(line.strip())
	regulatorsFile.close()
	individualInteractors = []
	for i in range(len(regulators)):
		# Create a new array for each regulator
		individualInteractors.append([])
	PPIFile = open(PPIFileName)
	PPIFile.readline()
	for line in PPIFile:
		# Iterate through interactions and record all genes that interact with regulators
		#lineElements = line.split("\t")
		#firstGene = lineElements[7]
		#secondGene = lineElements[8]
		lineElements = line.split(",")
		firstGene = lineElements[1]
		secondGene = lineElements[3]
		for i in range(len(regulators)):
			# Iterate through regulators and add interactors to their arrays
			if firstGene == regulators[i]:
				# The first gene is a regulator, so add the second gene to the regulator's list of interactors
				individualInteractors[i].append(secondGene)
				continue
			#if secondGene == regulators[i]:
			#	# The second gene is a regulator, so add the first gene to the regulator's list of interactors
			#	individualInteractors[i].append(firstGene)
	PPIFile.close()
	print len(individualInteractors[0])
	print len(individualInteractors[1])
	return [individualInteractors, regulators]

def getCommonInteractors(individualInteractors, regulators, commonInteractorsFileName):
	# Find all of the genes that interact with all of the regulators and write them to a file
	commonInteractorsFile = open(commonInteractorsFileName, 'w+')
	for gene in individualInteractors[0]:
		# Iterate through genes that interact with the first regulator and find the ones that interact with all of the other regulators
		noInteractionFound = False
		for individualInteractorArray in individualInteractors[1:]:
			# Iterate through other regulators and set noInteractionFound to True if the gene does not interact with at least 1 of them
			if gene not in individualInteractorArray:
				# The gene does not interact with a regulator
				noInteractionFound = True
				continue
		if noInteractionFound == False:
			commonInteractorsFile.write(gene)
			commonInteractorsFile.write("\n")

if __name__=="__main__":
    import sys
    PPIFileName = sys.argv[1]
    regulatorsFileName = sys.argv[2]
    commonInteractorsFileName = sys.argv[3]
    [individualInteractors, regulators] = getIndividualInteractors(PPIFileName, regulatorsFileName)
    getCommonInteractors(individualInteractors, regulators, commonInteractorsFileName)
