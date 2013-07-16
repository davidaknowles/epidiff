import subprocess,os,sys
from mymerge import mymerge

def file_len(fname):
    p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE, 
                                              stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])


def myCall(cmd,linesToSkip=0):
    p=subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for i in range(linesToSkip):
        p.stdout.readline()
    
    return p.stdout.readline()

def jaccard(fn1,fn2,slop=1000,gen="~/P01Project/src/chromInfo.tab"):
    if slop > 0:
        os.system("bedtools slop -i %s -g %s -b %i > temp1" % (fn1,gen,slop))
        os.system("sort -u -k1,1 -k2,2n -k3,3n temp1 > temp1.sorted")
        os.system("bedtools merge -i temp1.sorted > temp1.merged")
        os.system("bedtools slop -i %s -g %s -b %i > temp2" % (fn2,gen,slop))
        os.system("sort -u -k1,1 -k2,2n -k3,3n temp2 > temp2.sorted")
        os.system("bedtools merge -i temp2.sorted > temp2.merged")
        fn1="temp1.merged"
        fn2="temp2.merged"
        
    mergefile="merge.temp"
    mymerge(fn1,fn2,mergefile) 
    size_union=file_len(mergefile)
    intersect_file="intersect.temp"
    os.system("bedtools intersect -a %s -b %s > %s" % (fn1,fn2,intersect_file))
    size_intersect=file_len(intersect_file)
    os.system("rm %s %s" % (intersect_file, mergefile)) 
    
    return float(size_intersect)/float(size_union)

if __name__=="__main__":
    print jaccard(sys.argv[1],sys.argv[2])