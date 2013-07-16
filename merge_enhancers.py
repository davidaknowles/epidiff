import os

def callEnhancersScript(path, cellTypeListFileName):
    # Make a script that will call enhancers
    cellTypeListFile = open(cellTypeListFileName)
    for line in cellTypeListFile:
        print line.strip()
        pathPline=path + line.strip()
#        os.system("bedtools merge -i " + pathPline + "_enhancers2.bed" + " > " + pathPline + "_enhancers3.bed")
        os.system("bedtools merge -i " + pathPline + "_enhancers_noH3K4me3.bed" + " > " + pathPline + "_enhancers_no_merged.bed")
    cellTypeListFile.close()

if __name__=="__main__":
    import sys
    path = "/afs/cs.stanford.edu/u/imk1/P01Project/QuEST_results/"
    cellTypeListFileName = "/afs/cs.stanford.edu/u/imk1/P01Project/src/cellList.txt"
    callEnhancersScript(path, cellTypeListFileName)
