import os, sys
sys.path.append('~/P01Project/src/')
from mymerge import mymerge
from great_query import great_query
from myjaccard import *



def myCall(cmd,linesToSkip=0):
    p=subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for i in range(linesToSkip):
        p.stdout.readline()
    
    return p.stdout.readline()

sets= [ [ ["Ei1","Ei2"] , ["EC","EC2"] ] , [ ["Fi1","Fi2"] , ["FB1","FB2"] ], [ ["Ci1","Ci2"] , ["CPC","CPC2"] ] , [ ["Ni1"], ["NSC"] ] ]

path = "/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/QuEST_results/"
enhancer_suffix="_enhancers_no_merged.bed"
for s in sets:
    ipsc=s[0]
    prog=s[1]
    
    if len(ipsc)>1:
        ipsc_all=path+ipsc[0]+"_all.bed"
        #mymerge(path+ipsc[0]+enhancer_suffix, path+ipsc[1]+enhancer_suffix, ipsc_all)
    else:
        ipsc_all=path+ipsc[0]+enhancer_suffix
    if len(prog)>1:
        prog_all=path+prog[0]+"_all.bed"
        #mymerge(path+prog[0]+enhancer_suffix, path+prog[1]+enhancer_suffix, prog_all)
    else:
        prog_all=path+prog[0]+enhancer_suffix
    
    res=path+"%s_minus_ESC.bed" % ipsc[0]
    os.system("bedtools subtract -a %s -b %sESC_slop.bed > %s" % (ipsc_all, path, res) )

myline=""
for t in sets:
    myline+=","+t[1][0]
print myline

for s in sets:
    ipsc=s[0]
    myline=ipsc[0]
    for t in sets:
        prog=t[1]
        if len(ipsc)>1:
            ipsc_all=path+ipsc[0]+"_all.bed"
            #mymerge(path+ipsc[0]+enhancer_suffix, path+ipsc[1]+enhancer_suffix, ipsc_all)
        else:
            ipsc_all=path+ipsc[0]+enhancer_suffix
        if len(prog)>1:
            prog_all=path+prog[0]+"_all.bed"
            #mymerge(path+prog[0]+enhancer_suffix, path+prog[1]+enhancer_suffix, prog_all)
        else:
            prog_all=path+prog[0]+enhancer_suffix
        res=path+"%s_minus_ESC.bed" % ipsc[0]
        #myline+=",%f"%jaccard(res,prog_all)
        myline+=",%f"%jaccard_with_slop(res,prog_all)
    print myline