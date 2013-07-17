
import sys

def giiaxToQuest(fileinName,fileoutName):
    filein=open(fileinName)
    fileout=open(fileoutName,"w")
    for l in filein:
        a=l.split()
        fileout.write(a[0]+" "+a[1]+" "+a[5]+"\n")

    filein.close()
    fileout.close()

if __name__ == "__main__":
    giiaxToQuest(sys.argv[1],sys.argv[2])

