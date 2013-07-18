import os, sys
import pylab
#cell1="Ni1"
#cell2="Ei1"
cell1=sys.argv[1]
cell2=sys.argv[2]
basedir="/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/QuEST_results/"
#suffix="_enhancers_noH3K4me3.bed"
suffix="_enhancers_no_merged.bed"
enhancer_file1=basedir+cell1+suffix
enhancer_file2=basedir+cell2+suffix
basedir2="/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/more_stats/"
ac_file1=open(basedir2+cell1+"_H3K27ac_stats.bed.sorted")
ac_file2=open(basedir2+cell2+"_H3K27ac_stats.bed.sorted")
os.system("cat %s %s > %s" % ( enhancer_file1, enhancer_file2, basedir+"temp" ))
os.system("sort -u -k1,1 -k2,2n -k3,3n %s > %s" % ( basedir+"temp", basedir+"temp2" ) )
os.system("mergeBed -i %s > %s" % ( basedir+"temp2", basedir+"temp3") )

def overlap( line1, line2 ): # -1: line1 < line2, 0: line1=line2, +1: line1 > line2
    a=line1.split()
    b=line2.split()
    if a[0] < b[0]:
        return -1
    if a[0] > b[0]:
        return +1
    if int(a[2]) < int(b[1]):
        return -1
    if int(a[1]) > int(b[2]):
        return +1
    return 0

curr_ac1=ac_file1.readline()
curr_ac2=ac_file2.readline()
f=open(basedir+"temp3")
out1=open("chip_to_plot.txt","w")
#out2=open("ef_to_plot.txt","w")
#out3=open("tag_ef_to_plot.txt","w")
for l in f:
    a=l.split()
    o=overlap( curr_ac1, l)
    while o==-1:
        curr_ac1=ac_file1.readline()
        o=overlap( curr_ac1, l)
    o2=overlap( curr_ac2, l)
    while o2==-1:
        curr_ac2=ac_file2.readline()
        o2=overlap( curr_ac2, l)
    if o==0 and o2==0:
        out1.write(curr_ac1.split()[3]+" "+curr_ac2.split()[3]+"\n")
        #out2.write(curr_ac1.split()[4]+" "+curr_ac2.split()[4]+"\n")
        #out3.write(curr_ac1.split()[5]+" "+curr_ac2.split()[5]+"\n")

out1.close()
#out2.close()
#out3.close()
f.close()
ac_file1.close()
ac_file2.close()
