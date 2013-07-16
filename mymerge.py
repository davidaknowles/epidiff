import sys, os

def mymerge(in1,in2,out):
    os.system("cat %s %s > cattemp" % (in1, in2))
    os.system("sort -u -k1,1 -k2,2n -k3,3n cattemp > sortfile")
    os.system("bedtools merge -i sortfile > %s" % out)
    os.system("rm cattemp sortfile")
    
if __name__=="__main__":
    mymerge(sys.argv[1],sys.argv[2],sys.argv[3])