from giiaxToQuest import giiaxToQuest
cell_lines_file=open("cellList.txt")
cell_lines=cell_lines_file.readlines()

import sys
import os
path="/srv/gs1/projects/snyder/imk1/P01Project/ChIPseqData/"
outputpath=path+"quest/"

fdr=0

marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "Pol2"]

mark_index=4

mark=marks[mark_index]

cell_line="Ei2"

questResultsDir="~/P01Project/dak_quest_results/" if fdr else "~/P01Project/quest_results_no_fdr/" 

print "******** Runnning quest, cell line: %s, mark: %s ************" % (cell_line, mark)

os.system("~/QuEST_2.4/run_QuEST_with_param_file.pl -ap " +  questResultsDir+cell_line+"_"+mark+"_new")

print "******** os.system call completed ************ "
