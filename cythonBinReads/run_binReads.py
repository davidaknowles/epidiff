from binReads import binReads
import pickle, sys
counts=binReads(sys.argv[1])
outputfileName=sys.argv[2]
with open(outputfileName,"wb") as f:
  pickle.dump(counts,f)