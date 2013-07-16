import os

def callEnhancersScript(path, cellTypeListFileName):
    # Make a script that will call enhancers
    cellTypeListFile = open(cellTypeListFileName)
    for line in cellTypeListFile:
        # Iterate through the cell types and make the script call enhancers for each
        temp1=path+"temp1"
        temp2=path+"temp2"
        pathPline=path + line.strip()
        slop1=path+"slop1"
        slop2=path+"slop2"
        os.system("bedtools slop -b 2000 -i %s -g chromInfo.txt > %s" % ( pathPline + "-GIIAX_H3K27ac_k_peaks.bed", slop1 ))
        os.system("bedtools slop -b 2000 -i %s -g chromInfo.txt > %s" % ( pathPline + "-GIIAX_H3K4me1_k_peaks.bed", slop2 ))
        os.system("intersectBed -a %s -b %s > %s " % ( slop1, pathPline + "-GIIAX_p300_k_peaks.bed", temp1) )
        os.system("intersectBed -a %s -b %s > %s " % ( temp1, pathPline + "-GIIAX_H3K4me1_k_peaks.bed", temp2) )
        os.system("bedtools subtract -a %s -b %s > %s " % ( temp2, pathPline + "-GIIAX_H3K4me3_k_peaks.bed", temp1 ) )
        os.system("sort -u -k1,1 -k2,2n -k3,3n " + temp1 + " > " + pathPline + "-GIIAX_EnhancerMerged2")
    cellTypeListFile.close()

if __name__=="__main__":
    import sys
    path = "/afs/cs.stanford.edu/u/imk1/P01Project/MACSResults/NonSubsamplePeaks/"
    cellTypeListFileName = "/afs/cs.stanford.edu/u/imk1/P01Project/src/cellList.txt"
    callEnhancersScript(path, cellTypeListFileName)
