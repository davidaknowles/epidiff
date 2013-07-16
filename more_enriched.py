# Compare two samples' acetylation at any position called as an active enhancer in either. 
# Output a list of outliers for both sample 1 and 2
import os, sys
import pylab
from numpy.random import randn
#cell1="Ni1"
#cell2="Ei1"
cell1=sys.argv[1]
cell2=sys.argv[2]
basedir="/afs/cs.stanford.edu/u/davidknowles/P01Project/QuEST_results/"
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

out2=open("chip_to_plot.txt","w")
#out3=open("tag_ef_to_plot.txt","w")
out2.write(cell1+" "+cell2+"\n")
region_dict={}
ac1_dict={}
ac2_dict={}
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
    ac1=0.0
    ac2=0.0
    if o==0:
        ac1=float(curr_ac1.split()[3])
    if o2==0:
        ac2=float(curr_ac2.split()[3])
        #out1.write(curr_ac1.split()[3]+" "+curr_ac2.split()[3]+"\n")
    diffo=ac1-ac2
    diff=diffo
    while region_dict.has_key(diff):
        diff=diffo+.1*randn()
    region_dict[ diff ] = l
    out2.write("%f %f\n" % (ac1,ac2) )
    ac1_dict[ diff ] = ac1
    ac2_dict[ diff ] = ac2
        #out2.write(curr_ac1.split()[4]+" "+curr_ac2.split()[4]+"\n")
        #out3.write(curr_ac1.split()[5]+" "+curr_ac2.split()[5]+"\n")
out2.close()
import numpy
from scipy import stats
x=numpy.array(ac1_dict.values())
y=numpy.array(ac2_dict.values())
#slope = stats.linregress(x,y)[0]
slope=1.0
newdiff={}
for i in region_dict:
    x=ac1_dict[i] 
    y=ac2_dict[i]
    if x==0.0:
        theta=numpy.pi/2.0
    else:
        theta=numpy.arctan(y/x)
    nd=numpy.sqrt(x*x+y*y)*numpy.sin(numpy.arctan(slope)-theta)
    print "%f %f" % (nd*numpy.sqrt(2),x-y)
    newdiff[nd]=i

out2.close()
#sorted_keys=region_dict.keys()
sorted_keys=newdiff.keys()
sorted_keys.sort()
N=int( float(len(region_dict))/20.0) 
out1=open(cell2+"_enriched.bed","w")
out2=open(cell2+"_points.txt","w")
for i in range(N):
    k=newdiff[sorted_keys[i]]
    out1.write( region_dict[ k ] ) 
    out2.write( "%f %f\n" % (ac1_dict[ k ], ac2_dict[k]) ) 
out1.close()
out2.close()

#sorted_keys=region_dict.keys()
sorted_keys=newdiff.keys()
sorted_keys.sort(reverse=1)
N=int( float(len(region_dict))/20.0) 
out1=open(cell1+"_enriched.bed","w")
out2=open(cell1+"_points.txt","w")
for i in range(N):
    k=newdiff[sorted_keys[i]]
    out1.write( region_dict[ k ] ) 
    out2.write( "%f %f\n" % (ac1_dict[ k ], ac2_dict[k]) ) 
out1.close()
out2.close()
#out2.close()
#out3.close()
f.close()
ac_file1.close()
ac_file2.close()
