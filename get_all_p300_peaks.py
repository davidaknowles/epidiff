from mymerge import mymerge
cell_lines_file=open("cellList.txt")
cell_lines=[x.strip() for x in cell_lines_file.readlines()]

import sys
import os
questResultsDir= "~/P01Project/quest_results_no_fdr/all/" 

first=1
for cell_line in cell_lines:
    fn=questResultsDir+cell_line+"_p300.bed"
    if first:
        os.system("cp %s temp" % fn)
    else:
        mymerge(fn,"temp","temp2")
        os.system("mv temp2 temp") 

os.system("mv temp all_p300.bed")
