import subprocess
import os

def jaccard(file1,file2):
    cmd=["bedtools","jaccard","-a",file1,"-b",file2]
    p=subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.stdout.readline()
    a=p.stdout.readline()
    return a.split()[2]

cellTypeListFile = open("/afs/cs.stanford.edu/u/imk1/P01Project/src/cellList.txt")
path="/afs/cs.stanford.edu/u/imk1/P01Project/MACSResults/PartialPeaks2/"
cellTypeList=cellTypeListFile.readlines()
cellTypeListFile.close()
iPSCs=["N","E","F","C"]

myLine=""
for cell in cellTypeList:
    myLine+=","+cell.strip()
print myLine
for i in iPSCs:
    fileName=path+i+"iOnly.bed"
    myLine = i+"i"
    for cell in cellTypeList:
        cells=cell.strip()
        myLine+=","+str(jaccard(fileName,path+cells+"-GIIAX_EnhancerMerged"))
    print myLine
