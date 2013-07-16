import os
marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "Pol2"]
cell_lines=[x+"pool" for x in ["Ci1","CPC","EC","Ei1","FB1","Fi1"]]

basedir="/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/QuEST_results/"
for cell_line in cell_lines:
    for mark in marks:
        fn=basedir+"%s_%s.bed" % (cell_line, mark)
        os.system("sort -u -k1,1 -k2,2n -k3,3n %s > %s.sorted" % (fn,fn))
        
        f=open("%s.sorted" % fn)
        o=open(basedir+"%s_%s.bed2.sorted" % (cell_line, mark),"w")
        firstline=1
        for l in f:
            if firstline:
                firstline=0
            else:
                a=l.split()
                if a[3][0]=="R":
                    o.write(l.replace(" ","\t")) 
        o.close() 
        f.close()
        