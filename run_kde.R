args=commandArgs(trailingOnly=T)
mark=args[1]
cell.line=args[2]
load("hg18.RData") 
load("kernels.RData") 
source("ChIP.R")
in.path="/srv/gs1/projects/snyder/imk1/P01Project/ChIPseqData/quest/"
out.path="/srv/gs1/projects/snyder/imk1/P01Project/kdes/"
Step=100
width=10000
Genome<-generate.genome.table(A,Step=Step)
a<-load.reads(paste(in.path,cell.line,"_","background",".quest",sep=""))
SHIFT<-calculate.shift(a,Genome)
print(SHIFT)
if (SHIFT>0)
   a<-shift(a,SHIFT)
KRN<-generate.kernel(name=mark,step=Step,width=width,source=kernels)
data.out<-ChIP(a,KRN,Step=Step,Genome=Genome)
save(data.out, file=paste(out.path,"/",cell.line,"_",mark,"_background.RData",sep=""))


