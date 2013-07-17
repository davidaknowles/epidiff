from giiaxToQuest import giiaxToQuest
cell_lines_file=open("cellList.txt")
cell_lines=cell_lines_file.readlines()
fdr=1
import sys
import os
marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "Pol2"]
questResultsDir="/srv/gs1/projects/snyder/imk1/P01Project/dak_quest_results/"
for mark in marks:
    for cell_line_raw in cell_lines:
        cell_line=cell_line_raw.strip()
        f=open(questResultsDir+cell_line+"_"+mark+"/calls/peak_caller.ChIP.out.accepted")
        o=open(questResultsDir+"all2/" + cell_line+"_"+mark + "_stats.bed","w")
        for l in f:
            a=l.split()
            if len(a)>0 and a[0][0]=='R':
                b=a[2].split("-")
                o.write(("%s"+"\t%s"*5+"\n") % ( a[1], b[0], b[1], a[4], a[10], a[16] ))
                
        f.close()
        o.close() 

        
        

