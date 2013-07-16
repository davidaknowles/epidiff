from numpy import *
import pylab
def binReadsByStrand(inputFileName, binSize=10, chromFile="/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/src/chromInfo.tab" ):
    countsPlus={}
    countsMinus={}
    with open(chromFile) as f: 
        for l in f:
            a=l.split()
            chrName=a[0]
            chrLength=int(a[1])
            nBins=ceil(float(chrLength)/float(binSize))+1
            countsPlus[chrName]=zeros(nBins,dtype=uint16)
            countsMinus[chrName]=zeros(nBins,dtype=uint16)

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
            offset=65
            if strand=="+":
                center=start+offset
            else:
                center=end-offset

            
            binIndex=int(floor(float(center)/float(binSize)))
            if strand=="+":
                
                countsPlus[chrName][binIndex]+=1
            else:
                countsMinus[chrName][binIndex]+=1            
           
    return (countsMinus,countsPlus)

def autocorr(inputFileName, binSize=10):
    (countsMinus,countsPlus)=binReadsByStrand(inputFileName,binSize) 
    
def slow_cross_corr(a,b,r=100,plot=False):
    a=a-mean(a)
    b=b-mean(b)
    res=zeros( 2*r+1 )
    for i in range(2*r+1):
        offset=-r+i
        tempa=a[ max(0,offset):min( len(a), len(a)+offset ) ]
        tempb=b[ max(0,-offset):min( len(a), len(a)-offset) ]
        assert( len(tempa) == len(tempb) )
        res[i]=dot(tempa,tempb)/float(len(tempa))
    if plot:
        pylab.plot( arange(-r,r+1), res ); 
        pylab.ylabel('cross correlation')
        pylab.show()
    return res
        
