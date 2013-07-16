fn="/afs/cs.stanford.edu/u/imk1/P01Project/MACSResults/IntersectedPeaks/enhancersFileNames"
with open(fn) as f:
    for l in f:
        print l.split("-")[0]
