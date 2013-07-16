import subprocess,os

def myCall(cmd,linesToSkip=0):
    p=subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for i in range(linesToSkip):
        p.stdout.readline()
    
    return p.stdout.readline()
    
def jaccard(fn1,fn2):
    jaccardline=myCall(["bedtools","jaccard","-a",fn1,"-b",fn2],linesToSkip=1)
    return float(jaccardline.split()[2])

def jaccard_with_slop(fn1,fn2,slop=2000,gen="~/P01Project/src/chromInfo.tab"):
    os.system("bedtools slop -i %s -g %s -b %i > temp1" % (fn1,gen,slop))
    os.system("bedtools slop -i %s -g %s -b %i > temp2" % (fn2,gen,slop))
    jaccardline=myCall(["bedtools","jaccard","-a","temp1","-b","temp2"],linesToSkip=1)
    os.system("rm temp1 temp2") 
    return float(jaccardline.split()[2])