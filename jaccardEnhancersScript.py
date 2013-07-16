
import os, sys
from myjaccard2 import jaccard

marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "Pol2"]

def jaccardEnhancersScript(path, cellsList,output,enhancer_suffix="_enhancers_no_merged.bed"):
    # Make a script that will intersect the enhancers and print the number of lines in each intersection

    myline=""
    for i in cellsList:
        myline += ","+i.strip()
    output.write(myline+"\n")
    
    for i in range(len(cellsList)):
        # Iterate through the enhancer files and get the intersection for each
        fileNameOne = path + cellsList[i].strip()+enhancer_suffix
        myline=cellsList[i].strip()
        for j in range(0,i):
            myline += ","
        for j in range(i, len(cellsList)):
            # Iterate through files for intersection
            fileNameTwo = path + cellsList[j].strip()+enhancer_suffix
            myline += ","+str(jaccard(fileNameOne,fileNameTwo))
        output.write(myline+"\n")


def runForEnhancers():
    #path = "/afs/cs.stanford.edu/u/imk1/P01Project/MACSResults/NonSubsamplePeaks/"
    #jaccardEnhancersScript(path, "cellList_minusEi2.txt")
    cellsFile = open("cellList.txt")
    cellsList = [x.strip() for x in cellsFile.readlines()]
    cellsFile.close()
    cellsList.append('ESC')
    cellsList += [x+"pool" for x in ["Ci1","CPC","EC","Ei1","FB1","Fi1"]]
    path = "/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/QuEST_results/"
    jaccardEnhancersScript(path, cellsList, sys.stdout)
    
def runForOtherMarks():
    for m in marks:
        print "-------------- %s ----------------" % m
        path = "/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/QuEST_results/"
        f=open(path+m+"_jaccard.csv","w") 
        jaccardEnhancersScript(path, "cellList.txt", f, enhancer_suffix="_%s.bed2.sorted"%m)
        f.close()


if __name__=="__main__":
    runForEnhancers()