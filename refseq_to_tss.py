import os, sys
f=open(sys.argv[1])
firstline=1
for l in f:
    if firstline:
        firstline=0
        continue
    else:
        a=l.split("\t")
        strand=a[3]
        tss=a[4] if strand=="+" else a[5]
        tss=int(tss)
        start=max(tss-1000,1)
        end=tss+1000
        print "%s\t%i\t%i" % (a[2],start,end)
