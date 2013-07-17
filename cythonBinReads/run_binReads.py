from binReads import binReads
import pickle, sys, os

def main(inputfileName,outputfileFilename):
  if os.path.exists(outputfileName):
    return
  counts=binReads(inputfileName)
  with open(outputfileName,"wb") as f:
    pickle.dump(counts,f)

if __name__ == "__main__":
  main(sys.argv[1],sys.argv[2])
