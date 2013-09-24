import os, sys
f=open(sys.argv[1])
g=open(sys.argv[2])
for m in g:
    l=f.readline()
    while l!=m:
        print 1
        l=f.readline()
    print 0
    
