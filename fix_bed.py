import sys, os
fn=sys.argv[1]
f=open(fn)
for l in f:
    a=l.split("\t")
    a[1]=str(max(int(a[1]),0))
    a[2]=str(max(int(a[2]),0))
    if int(a[1])<int(a[2]):
        print "\t".join(a)
