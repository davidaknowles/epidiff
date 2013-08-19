cell_lines_file=open("cellList.txt")
cell_lines=cell_lines_file.readlines()
cell_lines.append("ESC")

import sys
import os
path="/srv/gs1/projects/snyder/imk1/P01Project/ChIPseqData/"
outputpath=path+"quest/"
i=int(sys.argv[1])-1

marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300"] #, "Pol2"]
#marks=["background"]
#mark="background"
cell_line_index=i/len(marks)
mark_index=i%len(marks)
mark=marks[mark_index]

cell_line=cell_lines[cell_line_index].strip()
print "Running kde_to_max.R for cell line %s, mark %s" % ( cell_line, mark)
os.system("/srv/gs1/software/R/R-3.0.1/bin/Rscript kde_to_max.R %s %s" % (mark,cell_line) )
