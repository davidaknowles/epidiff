import sys
f = open(sys.argv[1])
if len(sys.argv)>2:
    split_by=sys.argv[2]
else:
    split_by=" "
for l in f:
    a=l.split(split_by)
    print "\t".join([x.strip() for x in a])
f.close()

