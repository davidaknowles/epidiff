cell_lines_file=open("cellList.txt")
cell_lines=cell_lines_file.readlines()
cell_lines.append("ESC")

import sys
import os
path="/srv/gs1/projects/snyder/imk1/P01Project/ChIPseqData/"
#outputpath=path+"quest/"
outputpath=path+"tomek_enhancers/"
try:
    os.makedirs(outputpath)
except OSError:
    pass
peaks_file="tomek_enhancers.bed"


marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300"] #, "Pol2"]
#marks=["background"]
#mark="background"

if len(sys.argv)==2:
    i=int(sys.argv[1])-1
    
    cell_line_index=i/len(marks)
    mark_index=i%len(marks)
    mark=marks[mark_index]
    
    cell_line=cell_lines[cell_line_index].strip()
    print "Running kde_to_max.R for cell line %s, mark %s" % ( cell_line, mark)
    os.system("/srv/gs1/software/R/R-3.0.1/bin/Rscript kde_to_max.R %s %s %s %s" % (mark,cell_line,peaks_file,outputpath) )
else:
    print "Need %i qsub jobs" % (len(marks)*len(cell_lines))
