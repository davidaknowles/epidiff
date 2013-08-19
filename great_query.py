import urllib, urllib2
import sys
import os
import pandas

tempfn="~/www/temp.bed"
baseUrl="http://bejerano.stanford.edu/great/public/cgi-bin/greatStart.php"

def great_query(fn):
    os.system("cp %s %s" % ( fn, tempfn ))
    
    data={}
    data['requestURL']="http://cs.stanford.edu/~davidknowles/temp.bed"
    data['requestSpecies']="hg18"
    data['outputType']="batch"
    encoded=urllib.urlencode(data)
    request=urllib2.urlopen(baseUrl + "?" + encoded)
    print baseUrl + "?" + encoded
    names=["Ontology", "ID", "Desc", "BinomRank", "BinomP", "BinomBonfP", "BinomFdrQ", "RegionFoldEnrich", "ExpRegions", "ObsRegions", "GenomeFrac", "SetCov", "HyperRank", "HyperP", "HyperBonfP", "HyperFdrQ", "GeneFoldEnrich", "ExpGenes", "ObsGenes", "TotalGenes", "GeneSetCov", "TermCov", "Regions", "Genes"]
    df=pandas.io.parsers.read_table(request,comment="#",skiprows=5,header=None,names=names)
    os.system("rm " + tempfn)
    request.close()
    f=df[(df['HyperFdrQ']<0.1) & (df['BinomFdrQ'] < 0.1) & (df['RegionFoldEnrich'] > 2.0) & (df['Ontology']=="GO Biological Process")]
    #f=df[(df['RegionFoldEnrich'] > 2.0) & (df['Ontology']=="GO Biological Process")]
    f=f.sort('BinomP')
    return f


if __name__=="__main__":
    cellTypeListFile = open("/afs/cs.stanford.edu/u/imk1/P01Project/src/cellList.txt")
    first_time=1

    for cell in cellTypeListFile:
        celln=cell.strip()
        #fn="/afs/cs.stanford.edu/u/imk1/P01Project/MACSResults/PartialPeaks2/%s-GIIAX_EnhancerMerged"  \% celln
        fn="/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/quest_enhancers/%s_enhancers_simp.bed" % celln
        
        f=great_query(fn)
        
        print celln, f.shape[0]
        if f.shape[0] > 0:
            f=f[['Ontology','ID','Desc','BinomFdrQ']].iloc[1:min(10,f.shape[0])]
            f['Cell']=celln
            
            if first_time:
                res=f
            else:
                res=res.append(f)
                
            first_time=0
    
    res=res.ix[:,['Cell','Ontology','ID','Desc','BinomFdrQ']]
    res.to_csv("GO_only.csv")
