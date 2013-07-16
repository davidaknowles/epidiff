def makeCallEnhancersScript(path, cellTypeListFileName, outputFileName):
	# Make a script that will call enhancers
	cellTypeListFile = open(cellTypeListFileName)
	outputFile = open(outputFileName, 'w+')
	for line in cellTypeListFile:
		# Iterate through the cell types and make the script call enhancers for each
		outputFile.write("intersectBed -a " + path + line.strip() + "-GIIAX_H3K27ac_Intersected -b " + path + line.strip() + "-GIIAX_H3K4me1_Intersected > " + path + line.strip() + "-GIIAX_EnhancerOne\n")
		outputFile.write("intersectBed -a " + path + line.strip() + "-GIIAX_H3K27ac_Intersected -b " + path + line.strip() + "-GIIAX_p300_Intersected > " + path + line.strip() + "-GIIAX_EnhancerTwo\n")
		outputFile.write("cat " + path + line.strip() + "-GIIAX_EnhancerOne " + path + line.strip() + "-GIIAX_EnhancerTwo > " + path + line.strip() + "-GIIAX_EnhancerCat\n")
		outputFile.write("sort -u -k1,1 -k2,2n -k3,3n " + path + line.strip() + "-GIIAX_EnhancerCat > " + path + line.strip() + "-GIIAX_EnhancerSorted\n")
		outputFile.write("mergeBed -i " + path + line.strip() + "-GIIAX_EnhancerSorted > " + path + line.strip() + "-GIIAX_EnhancerMerged\n")
	cellTypeListFile.close()
	outputFile.close()

if __name__=="__main__":
    import sys
    path = sys.argv[1]
    cellTypeListFileName = sys.argv[2]
    outputFileName = sys.argv[3]
    makeCallEnhancersScript(path, cellTypeListFileName, outputFileName)
