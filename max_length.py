import sys, os
fn=sys.argv[1]
f=open(fn)
min_len=0
m=0
for l in f:
    a=l.split("\t")
    le=int(a[2])-int(a[1])
    m=max(le,m)
    min_len=min(le,min_len)
print min_len,m
f.close()
