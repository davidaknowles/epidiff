import os

def callEnhancer(path, cellline):
    # Iterate through the cell types and make the script call enhancers for each
    temp1=path+"temp1"
    temp2=path+"temp2"
    pathPline=path + cellline
    slop1=path+"slop1"
    slop2=path+"slop2"
    os.system("bedtools slop -b 2000 -i %s -g chromInfo.txt > %s" % ( pathPline + "_H3K27ac.bed2.sorted", slop1 ))
    os.system("bedtools slop -b 2000 -i %s -g chromInfo.txt > %s" % ( pathPline + "_H3K4me1.bed2.sorted", slop2 ))
    os.system("bedtools intersect -a %s -b %s > %s " % ( slop1, pathPline + "_p300.bed2.sorted", temp1) )
    os.system("bedtools intersect -a %s -b %s > %s " % ( temp1, slop2, temp2) )
    if 1:
        os.system("bedtools subtract -a %s -b %s > %s " % ( temp2, pathPline + "_H3K4me3.bed2.sorted", temp1 ) )
        os.system("sort -u -k1,1 -k2,2n -k3,3n " + temp1 + " > " + pathPline + "_enhancers_noH3K4me3.bed")
        os.system("bedtools merge -i %s > %s" % ( pathPline + "_enhancers_noH3K4me3.bed" , pathPline + "_enhancers_no_merged.bed" ))
    else: 
        os.system("sort -u -k1,1 -k2,2n -k3,3n " + temp2 + " > " + pathPline + "_enhancers2.bed")

def callEnhancersScript(path, cellTypeListFileName):
    # Make a script that will call enhancers
    cellTypeListFile = open(cellTypeListFileName)
    for line in cellTypeListFile:
        print line.strip()
        callEnhancer(path, line.strip())
    cellTypeListFile.close()

def callPoolEnhancers(path):
    cell_lines=[x+"pool" for x in ["Ci1","CPC","EC","Ei1","FB1","Fi1"]]
    for cl in cell_lines:
        print cl
        callEnhancer(path, cl)

if __name__=="__main__":
    import sys
    #path = "/afs/cs.stanford.edu/u/imk1/P01Project/QuEST_results/"
    path = "/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/QuEST_results/"
    #cellTypeListFileName = "/afs/cs.stanford.edu/u/imk1/P01Project/src/cellList.txt"
    #callEnhancersScript(path, cellTypeListFileName)
    #callEnhancer(path, "Ei2")
    callPoolEnhancers(path)