
from giiaxToQuest import giiaxToQuest

cell_lines=[["Ci1","Ci2"],["CPC","CPC2"],["EC","EC2"],["Ei1","Ei2"],["FB1","FB2"],["Fi1","Fi2"]]

import sys
import os
path="/srv/gs1/projects/snyder/imk1/P01Project/ChIPseqData/"
outputpath=path+"quest/"

marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "Pol2"]
marks.append("background")

for cell_line_pair in cell_lines:
    for mark in marks:
        in1=outputpath+cell_line_pair[0]+"_"+mark+".quest"
        in2=outputpath+cell_line_pair[1]+"_"+mark+".quest"
        os.system("cat %s %s > cattemp" % (in1, in2))
        outputfn=outputpath+"%spool_%s.quest" % (cell_line_pair[0], mark)
        os.system("sort -u -k1,1 -k2,2n -k3,3n cattemp > " + outputfn)
