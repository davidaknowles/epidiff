import urllib, urllib2
import sys
import os
import pandas, numpy
tempfn="~/www/temp.bed"
cellTypeListFile = open("/afs/cs.stanford.edu/u/imk1/P01Project/src/cellList.txt")

first_time=1

for cell in cellTypeListFile:
    celln=cell.strip()
    fn="/afs/cs.stanford.edu/u/imk1/P01Project/MACSResults/PartialPeaks2/%s-GIIAX_EnhancerMerged" % celln
    os.system("cp %s %s" % ( fn, tempfn ))
    baseUrl="http://bejerano.stanford.edu/great/public/cgi-bin/greatStart.php"
    data={}
    data['requestURL']="http://cs.stanford.edu/~davidknowles/temp.bed"
    data['requestSpecies']="hg18"
    data['outputType']="batch"
    encoded=urllib.urlencode(data)
    request=urllib2.urlopen(baseUrl + "?" + encoded)
    names=["Ontology", "ID", "Desc", "BinomRank", "BinomP", "BinomBonfP", "BinomFdrQ", "RegionFoldEnrich", "ExpRegions", "ObsRegions", "GenomeFrac", "SetCov", "HyperRank", "HyperP", "HyperBonfP", "HyperFdrQ", "GeneFoldEnrich", "ExpGenes", "ObsGenes", "TotalGenes", "GeneSetCov", "TermCov", "Regions", "Genes"]
    df=pandas.io.parsers.read_table(request,comment="#",skiprows=5,header=None,names=names)
    os.system("rm " + tempfn)
    request.close()
    #f=df[(df['HyperFdrQ']<0.05) & (df['BinomFdrQ'] < 0.05) & (df['RegionFoldEnrich'] > 2.0) & (df['Ontology']=="GO Biological Process")]
    f=df.sort('BinomFdrQ')
    stat=0.0
    stat2=0.0
    for i in range(f.shape[0]):
        s=f["Desc"][i]
        if type(s)==type("a") and "endotheli" in s.lower():
            stat+=1.0/float(i+1.0)
            
            stat2+= -numpy.log10(f["BinomP"][i]) if f["BinomP"][i]>0.0 else 50.0
            #print str(f["BinomP"][i])
    print "%s %f %f" % (cell.strip() , stat, stat2)
    
    