import sys
import os
path="/srv/gs1/projects/snyder/imk1/P01Project/ChIPseqData/"
outputpath=path+"quest/"
i=int(sys.argv[1])-1

marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "input"]

mark_index=i
mark=marks[mark_index]

cell_line="ESC"

os.system("/srv/gs1/software/R/R-3.0.1/bin/Rscript run_kde.R %s %s" % (mark,cell_line) )
