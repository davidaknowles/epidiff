# Find active enhancers specific to each iPSC (i.e. not in the other iPSCs)
import os
from mymerge import mymerge
cellTypeListFile = open("/afs/cs.stanford.edu/u/imk1/P01Project/src/cellList.txt")
path="/afs/cs.stanford.edu/u/imk1/P01Project/QuEST_results/"
outpath="/afs/cs.stanford.edu/u/davidknowles/scratch/"
iPSCs=["N","E","F","C"]
for i in iPSCs:
    current_file=outpath + i+"iOnly.bed"
    mymerge(path+i+"i1_enhancers3.bed",path+i+"i2_enhancers3.bed",current_file)
    tempfile=outpath + "temp"
    other_ipsc=[]
    for j in iPSCs:
        if j!=i:
            other_ipsc.append(j+"i1")
            other_ipsc.append(j+"i2")
    for ip in other_ipsc:
        os.system("bedtools subtract -a %s -b %s > %s" % ( current_file, path+ip+"_enhancers3.bed", tempfile))
        os.system("mv %s %s" % ( tempfile, current_file ))