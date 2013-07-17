from mycompare import compare
import sys, os, pickle
path="/srv/gs1/projects/snyder/imk1/P01Project/ChIPseqData/"
resultsDir=path+"pickled_counts/"

cell_lines_file=open("../cellList.txt")
cell_lines=cell_lines_file.readlines()
i=int(sys.argv[1])-1
num_cell_lines=len(cell_lines)
num_comparisons=((num_cell_lines+1)*(num_cell_lines))/2
marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "Pol2"]
mark_index=i/num_comparisons
mark=marks[mark_index]
comparison_index=i%num_comparisons

def getCells(num_cell_lines,comparison_index):
  for cell1 in range(num_cell_lines):
    for cell2 in range(cell1,num_cell_lines):
      if comparison_index==0:
        return (cell1,cell2)
      else:
        comparison_index-=1

(cell1,cell2)=getCells(num_cell_lines,comparison_index)
    
cell_line1=cell_lines[cell1].strip()
cell_line2=cell_lines[cell2].strip()

print "Comparing, cell lines: %s and %s, mark: %s" % (cell_line1, cell_line2, mark)

sample1=resultsDir+cell_line1+"_"+mark+"_counts.pickle"
sample2=resultsDir+cell_line2+"_"+mark+"_counts.pickle"
background1=resultsDir+cell_line1+"_Input_counts.pickle"
background2=resultsDir+cell_line2+"_Input_counts.pickle"
with open(sample1,"rb") as f:
    sample1=pickle.load(f)
with open(background1,"rb") as f:
    background1=pickle.load(f)
with open(sample2,"rb") as f:
    sample2=pickle.load(f)
with open(background2,"rb") as f:
    background2=pickle.load(f)

res=compare(sample1,background1,sample2,background2)

outputfileName=resultsDir+"%s_%s_%s.pickle"%(cell_line1,cell_line2,mark)
with open(outputfileName,"wb") as f:
  pickle.dump(res,f)

print "Finished"
