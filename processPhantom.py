from giiaxToQuest import giiaxToQuest
cell_lines_file=open("cellList.txt")
cell_lines=cell_lines_file.readlines()
fdr=1
import sys
import os
marks=["H3K27ac", "H3K27me3", "H3K4me1", "H3K4me3", "p300", "Pol2"]

f=open("/home/dak33/phantom.results")
res={}
res2={}
for l in f:
    a=l.split()
    cell_line=a[0].split("-")[0]
    mark=a[0].split("_")[1]
    if not res.has_key(cell_line):
        res[cell_line]={}
        res2[cell_line]={}
        
    res[cell_line][mark]=a[8]
    res2[cell_line][mark]=a[9]

myline = " " 
for mark in marks:
    myline += " & " + mark 
print myline+" \\\\ "

for cell_line_raw in cell_lines:
    cell_line=cell_line_raw.strip()
    myline=cell_line
    for mark in marks:
        myline+=" & " + res[cell_line][mark]
    print myline+" \\\\ "

myline = " " 
for mark in marks:
    myline += " & " + mark         
print myline+" \\\\ "

for cell_line_raw in cell_lines:
    cell_line=cell_line_raw.strip()
    myline=cell_line
    for mark in marks:
        myline+=" & " + res2[cell_line][mark]
    print myline+" \\\\ "
    


        
        

