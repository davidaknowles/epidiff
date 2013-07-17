
from giiaxToQuest import giiaxToQuest

cell_lines=[["Ci1","Ci2"],["CPC","CPC2"],["EC","EC2"],["Ei1","Ei2"],["FB1","FB2"],["Fi1","Fi2"]]

import sys
import os

marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "Pol2"]
fdr=0
questResultsDir="~/P01Project/dak_quest_results/" if fdr else "~/P01Project/quest_results_no_fdr/" 

for mark in marks:
    for cell_line_pair in cell_lines:
        cell_line=cell_line_pair[0]+"pool"
        fn=questResultsDir+cell_line+"_"+mark+"/tracks/ChIP_calls.filtered.bed"
        os.system("cp %s %sall/%s_%s.bed" % ( fn , questResultsDir, cell_line, mark))

