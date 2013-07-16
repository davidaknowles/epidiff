from numpy import *

def binReads(inputFileName, offset=100, binSize=200, chromFile="/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/src/chromInfo.tab" ):
    counts={}
    with open(chromFile) as f: 
        for l in f:
            a=l.split()
            chrName=a[0]
            chrLength=int(a[1])
            nBins=ceil(float(chrLength)/float(binSize))+1
            counts[chrName]=zeros(nBins,dtype=uint16)

    counter=0
    with open(inputFileName) as f:
        for l in f:
            counter +=1
            if counter % 100000 == 0:
                print counter/3e7
            a=l.split()
            chrName=a[0]
            start=int(a[1])
            end=int(a[2])
            strand=a[5]
            if strand=="+":
                center=start+offset
            else:
                center=end-offset
            binIndex=int(floor(float(center)/float(binSize)))
            counts[chrName][binIndex]+=1
    return counts

