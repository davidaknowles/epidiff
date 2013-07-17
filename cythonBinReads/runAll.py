from binReads import binReads
cell_lines_file=open("../cellList.txt")
cell_lines=cell_lines_file.readlines()

import sys, os, pickle

path="/srv/gs1/projects/snyder/imk1/P01Project/ChIPseqData/"
i=int(sys.argv[1])-1
marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "Pol2","Input"]
cell_line_index=i/len(marks)
mark_index=i%len(marks)
mark=marks[mark_index]
cell_line=cell_lines[cell_line_index].strip()
input_file=path+cell_line+"-GIIAX_"+mark+"_Sorted.NoBlack.tagAlign"
resultsDir=path+"pickled_counts/"
print "Binning reads, cell line: %s, mark: %s" % (cell_line, mark)

counts=binReads(input_file)
outputfileName=resultsDir+cell_line+"_"+mark+"_counts.pickle"
with open(outputfileName,"wb") as f:
  pickle.dump(counts,f)

print "Finished"
