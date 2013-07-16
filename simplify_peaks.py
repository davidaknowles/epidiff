import os
marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "Pol2"]
cellTypeListFileName = "/afs/cs.stanford.edu/u/imk1/P01Project/src/cellList.txt"
cell_lines_file=open(cellTypeListFileName)
cell_lines=cell_lines_file.readlines() 
cell_lines_file.close()
for cell_line_raw in cell_lines:
    cell_line=cell_line_raw.strip()
    oname="/afs/cs.stanford.edu/u/imk1/P01Project/QuEST_results/%s_all2.bed" % cell_line
    o=open(oname,"w")
    #o.write("track name=%s description=%s visibility=1\n" % ( "enhancer", "enhancer"))
    o2=open("/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/quest_enhancers/%s_enhancers_simp.bed" % cell_line,"w")
    
    f=open("/afs/cs.stanford.edu/u/imk1/P01Project/QuEST_results/%s_%s.bed" % (cell_line, "enhancers2"))
    for l in f:
        a=l.split()
        line="%s\t%s\t%s\n" % ( a[0], a[1], a[2] )
        #o.write(line)
        o2.write(line)
    f.close()
    o2.close()
    
    #for mark in marks:
        #o.write("track name=%s description=%s visibility=1\n" % (mark, mark))
        #f=open("/afs/cs.stanford.edu/u/imk1/P01Project/QuEST_results/%s_%s.bed" % (cell_line, mark))
        
        #firstline=1
        #for l in f:
            #if firstline:
                #firstline=0
            #else:
                #a=l.split()
                #o.write("%s\t%s\t%s\n" % ( a[0], a[1], a[2] ) )
        #f.close()
        
    #o.close()
    
    #os.system("gzip < %s > %s.gz" % ( oname, oname ) )