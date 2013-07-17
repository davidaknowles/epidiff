from giiaxToQuest import giiaxToQuest
cell_lines_file=open("cellList.txt")
cell_lines=cell_lines_file.readlines()

import sys
import os
path="/srv/gs1/projects/snyder/imk1/P01Project/ChIPseqData/"
outputpath=path+"quest/"
i=int(sys.argv[1])-1
fdr=int(sys.argv[2])

marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "Pol2"]
kinds=[3,3,3,3,1,2]
cell_line_index=i/len(marks)
mark_index=i%len(marks)
mark=marks[mark_index]

cell_line=cell_lines[cell_line_index].strip()
background_fn=outputpath+cell_line+"_background.quest"
input_file=path+cell_line+"-GIIAX_"+mark+"_Sorted.NoBlack"
quest_fn=outputpath+cell_line+"_"+mark+".quest"

#already done
#print "Converting %s to %s" % ( input_file, quest_fn )
#giiaxToQuest( input_file, quest_fn )

questResultsDir="~/P01Project/dak_quest_results/" if fdr else "~/P01Project/quest_results_no_fdr/" 


print "Runnning quest, cell line: %s, mark: %s" % (cell_line, mark)

os.system("~/QuEST_2.4/generate_QuEST_parameters.pl -QuEST_align_ChIP %s -QuEST_align_RX_noIP %s -gt ~/P01code/chromInfo2.txt -ap %s -kind %s -params 3 %s" % (quest_fn, background_fn, questResultsDir+cell_line+"_"+mark, str(kinds[mark_index]), "-fdr" if fdr else "" ) )

print "---------- completed ---------------"
