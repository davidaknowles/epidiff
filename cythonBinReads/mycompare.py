import scipy, pickle, sys
from scipy.special import gammaln
from numpy import *
import pdb 

def gammaLogNormaliser(a,b):
### log normaliser for a gamma distribution with shape a and rate b
    return a*log(b)-gammaln(a)

def evidence( obs, a, b ):
### obs should be a list of narrays, (a,b) are the Gamma hypers
    return -sum([gammaln(x+1) for x in obs])+gammaLogNormaliser(a,b)-gammaLogNormaliser(a+sum(obs),b+len(obs))


def evidence2( obs, a, b ):
### obs should be a list of narrays, (a,b) are the Gamma hyper
    if len(obs)==1:
        return -gammaln(obs[0]+1)+gammaLogNormaliser(a,b)-gammaLogNormaliser(a+obs[0],b+len(obs))
    else:
        return -sum([gammaln(x+1) for x in obs],axis=0)+gammaLogNormaliser(a,b)-gammaLogNormaliser(a+sum(obs,axis=0),b+len(obs))

def detectDifference(o,a=0.01,b=0.01):
### o[i][j]: i indexes the sample, j=0 for background, j=1 for sample (or visa versa)
    pSameL=zeros(len(o))
    pDiffL=zeros(len(o))
    for i in range(2):
        s=o[i]
        pSameL[i]=evidence( s, a, b )
        pDiffL[i]=sum( [evidence([x], a, b) for x in s],  )
    pa=.5
    logpa=log(pa)
    logpNotA=log(1.0-pa)
    logPOgivenAis1=log(sum(exp([sum(pSameL)+logpa,sum(pDiffL)+logpNotA])))
    logPOgivenAis0=log(sum(exp([pSameL[0]+logpa,pDiffL[0]+logpNotA])))+log(sum(exp([pSameL[1]+logpa,pDiffL[1]+logpNotA])))
    return logPOgivenAis0-logPOgivenAis1

def compareToBackground(s,a,b):
    pSameL=evidence2( s, a, b )
    pDiffL=sum( [evidence2([x], a, b) for x in s], axis=0 )
    return (pSameL,pDiffL)

def detectDifference2(o,a=0.01,b=0.01,pa=0.5):
    ### o[i][j]: i indexes the sample, j=0 for background, j=1 for sample (or visa versa)
    chrLen=len(o[0][0])
    pSameL=zeros((len(o),chrLen))
    pDiffL=zeros((len(o),chrLen))
    for i in range(2):
        (pSameL[i,:],pDiffL[i,:])=compareToBackground(o[i],a,b)
    logpa=log(pa)
    logpNotA=log(1.0-pa)
#    pdb.set_trace()
    logPOgivenAis1=log(sum(exp([sum(pSameL,axis=0)+logpa,sum(pDiffL,axis=0)+logpNotA]),axis=0))
    logPOgivenAis0=log(sum(exp([pSameL[0]+logpa,pDiffL[0]+logpNotA]),axis=0))+log(sum(exp([pSameL[1]+logpa,pDiffL[1]+logpNotA]),axis=0))
    return logPOgivenAis0-logPOgivenAis1

def detectDifferenceRangePa(o,parange,a=0.01,b=0.01):
    ### o[i][j]: i indexes the sample, j=0 for background, j=1 for sample (or visa versa)
    chrLen=len(o[0][0])
    pSameL=zeros((len(o),chrLen))
    pDiffL=zeros((len(o),chrLen))
    for i in range(2):
        (pSameL[i,:],pDiffL[i,:])=compareToBackground(o[i],a,b)
    res=zeros(len(parange))
    for i in range(len(parange)):
        pa=parange[i]
        logpa=log(pa)
        logpNotA=log(1.0-pa)
        logPOgivenAis1=log(sum(exp([sum(pSameL,axis=0)+logpa,sum(pDiffL,axis=0)+logpNotA]),axis=0))
        logPOgivenAis0=log(sum(exp([pSameL[0]+logpa,pDiffL[0]+logpNotA]),axis=0))+log(sum(exp([pSameL[1]+logpa,pDiffL[1]+logpNotA]),axis=0))
        res[i]=sum(logPOgivenAis0)-sum(logPOgivenAis1)
    return res

#o=array([[100,150],[200,300]])
#print("Log evidence for difference: %f" % detectDifference(o)

def compare(sample1,background1,sample2,background2):
    res={}
    for chromo in sample1:
        print chromo
        chrLen=len(sample1[chromo])
        res[chromo]=zeros(chrLen)
        for binIndex in range(chrLen):
            res[chromo][binIndex]=detectDifference( array( [[sample1[chromo][binIndex],background1[chromo][binIndex]],[sample2[chromo][binIndex],background2[chromo][binIndex]]] ))
    return res


def compare2(sample1,background1,sample2,background2):
    res={}
    for chromo in sample1:
        print chromo
        res[chromo]=detectDifference2( array( [[sample1[chromo],background1[chromo]],[sample2[chromo],background2[chromo]]] ))
    return res

if __name__=="__main__":
    if len(sys.argv)==1:
        print detectDifference( [[100,150],[200,300]] )
    else:

        with open(sys.argv[1],"rb") as f:
            sample1=pickle.load(f)
        with open(sys.argv[2],"rb") as f:
            background1=pickle.load(f)
        with open(sys.argv[3],"rb") as f:
            sample2=pickle.load(f)
        with open(sys.argv[4],"rb") as f:
            background2=pickle.load(f)
        res=compare2(sample1,background1,sample2,background2)
        with open(sys.argv[5],"wb") as f:
            pickle.dump(res,f)
