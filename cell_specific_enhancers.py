# Find active enhancers in the progenitor and derived iPSCs (and not in H9 ESCs) 
import os, sys
sys.path.append('~/P01Project/src/')
from mymerge import mymerge
from great_query import great_query

#sets= [ [ ["Ei1","Ei2"] , ["EC","EC2"] ] , [ ["Fi1","Fi2"] , ["FB1","FB2"] ], [ ["Ci1","Ci2"] , ["CPC","CPC2"] ] , [ ["Ni1"], ["NSC"] ] ]
sets= [ [ ["Ei1pool"] , ["ECpool"] ] , [ ["Fi1pool"] , ["FB1pool"] ], [ ["Ci1pool"] , ["CPCpool"] ] , [ ["Ni1"], ["NSC"] ] ]

path = "/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/QuEST_results/"
enhancer_suffix="_enhancers_no_merged.bed"
for s in sets:
    ipsc=s[0]
    prog=s[1]
    
    if len(ipsc)>1:
        ipsc_all=path+ipsc[0]+"_all.bed"
        mymerge(path+ipsc[0]+enhancer_suffix, path+ipsc[1]+enhancer_suffix, ipsc_all)
    else:
        ipsc_all=path+ipsc[0]+enhancer_suffix
    if len(prog)>1:
        prog_all=path+prog[0]+"_all.bed"
        mymerge(path+prog[0]+enhancer_suffix, path+prog[1]+enhancer_suffix, prog_all)
    else:
        prog_all=path+prog[0]+enhancer_suffix
    res=path+"%s_and_%s.bed" % (ipsc[0],prog[0]) 
    os.system("bedtools intersect -a %s -b %s > %s" % (ipsc_all, prog_all, res) )
    os.system("wc " + res) 
    res2=path+"%s_and_%s_minus_ESC.bed" % (ipsc[0],prog[0])
    os.system("bedtools subtract -a %s -b %sESC_slop.bed > %s" % (res, path, res2) )
    os.system("wc " + res2) 
    go=great_query(res)
    print go.shape
    go=go[['Ontology','ID','Desc','BinomFdrQ']].iloc[1:min(20,go.shape[0])]
    go.to_csv(path+"%s_and_%s_go.csv" % (ipsc[0],prog[0]) )
    
    go=great_query(res2)
    print go.shape
    go=go[['Ontology','ID','Desc','BinomFdrQ']].iloc[1:min(20,go.shape[0])]
    go.to_csv(path+"%s_and_%s_minus_ESC_go.csv" % (ipsc[0],prog[0]) )
