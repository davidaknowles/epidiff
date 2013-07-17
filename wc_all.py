cell_lines_file=open("cellList.txt")
cell_lines=cell_lines_file.readlines()
cell_lines=[["Ci1","Ci2"],["CPC","CPC2"],["EC","EC2"],["Ei1","Ei2"],["FB1","FB2"],["Fi1","Fi2"]]

import subprocess
import os

def file_len(fname):
    p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE, 
                                              stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])

import sys
import os
marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "Pol2"]
#questResultsDir="/srv/gs1/projects/snyder/imk1/P01Project/ChIPseqData/"
#questResultsDir="/srv/gs1/projects/snyder/imk1/P01Project/dak_quest_results/all/"
questResultsDir="/srv/gs1/projects/snyder/imk1/P01Project/quest_results_no_fdr/"
 
myline=""
for mark in marks:
    myline+=" & " + mark
print myline + " \\\\ "



for cell_line_raw in cell_lines:
#    cell_line=cell_line_raw.strip()
    cell_line=cell_line_raw[0]+"pool"
    myline=cell_line
    for mark in marks:
        #fn=questResultsDir+cell_line+"_"+mark+".bed"
#        fn=questResultsDir+cell_line+"-GIIAX_"+mark+"_Sorted.NoBlack"
        fn=questResultsDir+cell_line+"_"+mark+"/tracks/ChIP_calls.filtered.bed"
        os.system("cp %s %s" % (fn , questResultsDir+"all/%s_%s.bed" % (cell_line, mark) ) )
        os.system("grep R- %s > temp" % fn)
        myline+=" & " + str( file_len( "temp" ) )
    print myline + " \\\\ "

os.system("rm temp")


        
        

