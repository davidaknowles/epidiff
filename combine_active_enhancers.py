import sys
import os
cellTypeListFile = open("/afs/cs.stanford.edu/u/imk1/P01Project/src/cellList.txt")
path="/afs/cs.stanford.edu/u/imk1/P01Project/MACSResults/NonSubsamplePeaks/"
outputfile=open(path+"allActiveEnhancers.bed",'w+')

for cell in cellTypeListFile:
    celln=cell.strip()
    outputfile.write("track name=%s description=\"%s\" \n" % ( celln , celln+" active enhancers" ))
    
    f=open(path + celln + "-GIIAX_EnhancerMerged")
    outputfile.write(f.read())
    f.close()
