def findGenesInLists(geneListFileName, genomeListFileName, foundListFileName):
	# For every gene, determine whether it has been found and, if it has not been found, whether it is in the human genome
	genomeListFile = open(genomeListFileName)
	genomeList = []
	for line in genomeListFile:
		# Convert all gene names to upper case
		genomeList.append(line.upper())
	genomeListFile.close()
	foundListFile = open(foundListFileName)
	foundList = []
	for line in foundListFile:
		# Convert all gene names to upper case
		foundList.append(line.upper())
	foundListFile.close()
	geneListFile = open(geneListFileName)
	for line in geneListFile:
		# Iterate through genes and print which ones have been found and which ones are not in the genome
		if line.upper() in foundList:
			# Gene has already been found
			print line + " found!"
			continue
		if line.upper() not in genomeList:
			# There is no gene with the name of the current gene in the human genome
			print line + " not in genome!"
	geneListFile.close()

if __name__=="__main__":
    import sys
    geneListFileName = sys.argv[1]
    genomeListFileName = sys.argv[2]
    foundListFileName = sys.argv[3]
    findGenesInLists(geneListFileName, genomeListFileName, foundListFileName)
