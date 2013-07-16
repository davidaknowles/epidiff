import sys
f = open(sys.argv[1])
for l in f:
    a=l.split()
    print "\t".join(a)
f.close()

