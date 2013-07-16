import os

def callEnhancersScript(path, cellTypeListFileName):
	# Make a script that will call enhancers
	cellTypeListFile = open(cellTypeListFileName)
	for line in cellTypeListFile:
		# Iterate through the cell types and make the script call enhancers for each
		os.system("intersectBed -a " + path + line.strip() + "-GIIAX_H3K27ac_Intersected -b " + path + line.strip() + "-GIIAX_H3K4me1_Intersected > " + path + line.strip() + "-GIIAX_EnhancerOne\n")
		os.system("intersectBed -a " + path + line.strip() + "-GIIAX_H3K27ac_Intersected -b " + path + line.strip() + "-GIIAX_p300_Intersected > " + path + line.strip() + "-GIIAX_EnhancerTwo\n")
		os.system("cat " + path + line.strip() + "-GIIAX_EnhancerOne " + path + line.strip() + "-GIIAX_EnhancerTwo > " + path + line.strip() + "-GIIAX_EnhancerCat\n")
		os.system("sort -u -k1,1 -k2,2n -k3,3n " + path + line.strip() + "-GIIAX_EnhancerCat > " + path + line.strip() + "-GIIAX_EnhancerSorted\n")
		os.system("mergeBed -i " + path + line.strip() + "-GIIAX_EnhancerSorted > " + path + line.strip() + "-GIIAX_EnhancerMerged\n")
	cellTypeListFile.close()

if __name__=="__main__":
    import sys
    path = "/afs/cs.stanford.edu/u/imk1/P01Project/MACSResults/PartialPeaks2/"
    cellTypeListFileName = "/afs/cs.stanford.edu/u/imk1/P01Project/src/cellList.txt"
    callEnhancersScript(path, cellTypeListFileName)
