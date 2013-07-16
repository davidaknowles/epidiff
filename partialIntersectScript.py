import os
from itertools import combinations 

def partialIntersectScript(fileNameListFileName, path, outputpath, numSubsamples, cutoff):
    # Create a script that intersects files from a list
    fileNameListFile = open(fileNameListFileName)
    fileNameList = fileNameListFile.readlines()
    fileNameIndex = 0
    assert(len(fileNameList) % numSubsamples == 0) 
    nToDo = len(fileNameList) / numSubsamples
    for merges in range(nToDo):
        
        allfiles = [path + fileNameList[j].strip() for j in range(merges*numSubsamples,(merges+1)*numSubsamples)]
        filesToMerge = []
        tempfilecounter=0
        for subset in combinations(allfiles, cutoff):
            intersectedFileName = outputpath + "temp" + str(tempfilecounter)
            os.system("cp " + subset[0] + " " + intersectedFileName) 
            tempfilecounter += 1
            temptemp=outputpath + "temptemp"
            for i in range(1,len(subset)):
                os.system("intersectBed -a " + intersectedFileName + " -b " + subset[i] + " > " + temptemp)
                os.system("mv " + temptemp + " " + intersectedFileName)
            filesToMerge.append(intersectedFileName)
            
        catfile=outputpath + "temp_cat_file"
        filesToMergeString = " ".join(filesToMerge)
        os.system("cat " + filesToMergeString + " > " + catfile + "\n")
        os.system("rm " + filesToMergeString ) 
        sortedfile=outputpath + "temp_sorted_file"
        os.system("sort -u -k1,1 -k2,2n -k3,3n " + catfile + " > " + sortedfile + "\n")
        fileNameElements = fileNameList[merges*numSubsamples].split("_")
        intersectedFileName = outputpath + fileNameElements[0] + "_" + fileNameElements[1] + "_Intersected"
        temp_merged_file=outputpath + "temp_merged_file"
        os.system("mergeBed -i " + sortedfile + " > " + intersectedFileName +"\n")
        print intersectedFileName
        
    fileNameListFile.close()
    
if __name__=="__main__":
    import sys
    
    fileNameListFileName = "/afs/cs.stanford.edu/u/imk1/P01Project/MACSResults/GIIAXMACSFileNames"
    path = "/afs/cs.stanford.edu/u/imk1/P01Project/MACSResults/SubsamplePeaks/"
    outputpath = "/afs/cs.stanford.edu/u/imk1/P01Project/MACSResults/PartialPeaks2/"
    partialIntersectScript(fileNameListFileName, path, outputpath, numSubsamples=4, cutoff=2)
