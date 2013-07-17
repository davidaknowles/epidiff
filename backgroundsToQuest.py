from giiaxToQuest import giiaxToQuest
cell_lines_file=open("cellList.txt")
cell_lines=cell_lines_file.readlines()

import sys
path="/srv/gs1/projects/snyder/imk1/P01Project/ChIPseqData/"
outputpath=path+"quest/"
cell_line=cell_lines[int(sys.argv[1])].strip()
fn=path+cell_line+"-GIIAX_Input_Sorted.NoBlack"
outputfn=outputpath+cell_line+"_background.quest"
giiaxToQuest(fn, outputfn)
