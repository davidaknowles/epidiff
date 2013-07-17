from giiaxToQuest import giiaxToQuest
cell_lines_file=open("cellList.txt")
cell_lines=cell_lines_file.readlines()

import sys
import os
path="/srv/gs1/projects/snyder/imk1/P01Project/ChIPseqData/"
outputpath=path+"quest/"

marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "Pol2"]
os.system("rm temp")
counter=1
for cell_line_raw in cell_lines:
    for mark in marks:
        cell_line=cell_line_raw.strip()
        #questResultsDir="/srv/gs1/projects/snyder/imk1/P01Project/dak_quest_results/"
        questResultsDir="/home/dak33/P01Project/quest_results_no_fdr/"
        #resdir=questResultsDir+cell_line+"_"+mark+"/calls/*.accepted"
        resdir=questResultsDir+cell_line+"_"+mark+"/tracks/ChIP_calls.filtered.bed"
        print "counter: %i cell line: %s, mark: %s" % (counter, cell_line, mark)
        counter += 1
        os.system("wc %s >> temp" % resdir)
        #os.system("cp %s %s" % ( resdir , questResultsDir + "all/" + cell_line+"_"+mark + ".bed" ) )
#        os.system("cp %s %s" % ( questResultsDir+cell_line+"_"+mark+"/tracks/wig_profiles/ChIP_normalized.profile.wig.gz",  questResultsDir+"all_wig/"+cell_line+"_"+mark+".wig.gz" ) )


