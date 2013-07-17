import sys
import os
path="/srv/gs1/projects/snyder/imk1/P01Project/ChIPseqData/"
outputpath=path+"quest/"
fdr=0

mark=sys.argv[2]
cell_line=sys.argv[1]
background_fn=outputpath+cell_line+"_background.quest"
input_file=path+cell_line+"-GIIAX_"+mark+"_Sorted.NoBlack"
quest_fn=outputpath+cell_line+"_"+mark+".quest"

questResultsDir="~/P01Project/dak_quest_results/" if fdr else "~/P01Project/quest_results_no_fdr/" 

print "Runnning quest, cell line: %s, mark: %s" % (cell_line, mark)

os.system("~/QuEST_2.4/generate_QuEST_parameters_old.pl -QuEST_align_ChIP %s -QuEST_align_RX_noIP %s -gt ~/P01code/chromInfo2.txt -ap %s" % (quest_fn, background_fn, questResultsDir+cell_line+"_"+mark ) )

print "---------- completed ---------------"
