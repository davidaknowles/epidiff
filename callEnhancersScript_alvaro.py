import os

path = "/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/p01_esc_chip/"

temp1=path+"temp1"
temp2=path+"temp2"
slop1=path+"slop1"
slop2=path+"slop2"
path=path + "GSM60229"
os.system("bedtools slop -b 2000 -i %s -g chromInfo.txt > %s" % ( path + "4_ESC_H3K27ac_calls.bed.sorted.tab", slop1 ))
os.system("bedtools slop -b 2000 -i %s -g chromInfo.txt > %s" % ( path + "5_ESC_H3K4me1_calls.bed.sorted.tab", slop2 ))
os.system("bedtools intersect -a %s -b %s > %s " % ( slop1, path + "1_ESC_p300_calls.bed.sorted.tab", temp1) )
os.system("bedtools intersect -a %s -b %s > %s " % ( temp1, slop2, temp2) )
if 1:
    os.system("bedtools subtract -a %s -b %s > %s " % ( temp2, path + "6_ESC_H3K4me3_calls.bed.sorted.tab", temp1 ) )
    os.system("sort -u -k1,1 -k2,2n -k3,3n " + temp1 + " > " + path + "_enhancers_noH3K4me.bed")
else: 
    os.system("sort -u -k1,1 -k2,2n -k3,3n " + temp2 + " > " + path + "_enhancers.bed")
