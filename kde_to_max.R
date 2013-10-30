run=function(mark="H3K27me3",cell.line="Ei1",suffix="",peaks.file="all_p300.bed",out.path="temp") 
{
    a=read.table(peaks.file,sep="\t") 
    load("hg18.RData") 
    source("ChIP.R")
    in.path="/srv/gs1/projects/snyder/imk1/P01Project/kdes/"
    Step=100
    width=10000
    Genome<-generate.genome.table(A,Step=Step)
    Genome$chr=as.character(Genome$chr)
    load(paste(in.path,"/",cell.line,"_",mark,suffix,".RData",sep=""))
    a$V1=as.character(a$V1)
#    ends=unlist(INDEXV(a$V1,a$V3,Genome,Step))
    # browser()
    # peaks=PEAKV(starts,ends,data.out)
    n.peaks=nrow(a)
    peaks=numeric(n.peaks)
    for (i in 1:n.peaks){
        if (i %% 1000 == 0) cat(i,"\n")
        start=INDEX(a$V1[i],a$V2[i],Genome,Step)
        end=INDEX(a$V1[i],a$V3[i],Genome,Step)
        if (length(start)==0 || length(end)==0 ||end-start==0)
            cat("warning! start=end, i=",i,' start=',start,' end=',end,'\n');
        peaks[i]=PEAK(start,end,data.out)
    }
    save(peaks,file=paste(out.path,"/",cell.line,"_",mark,suffix,"_peaks.RData",sep=""))
}

if (!interactive())
{
    args=commandArgs(trailingOnly=T)
    run(args[1],args[2],"",args[3],args[4])
    run(args[1],args[2],"_background",args[3],args[4])
}

## a=read.table(peaks.file,sep="\t") 
## load("hg18.RData") 
## source("ChIP.R")
## in.path="/srv/gs1/projects/snyder/imk1/P01Project/kdes/"
## Step=100
## width=10000
## Genome<-generate.genome.table(A,Step=Step)
## Genome$chr=as.character(Genome$chr)

## a$V1=as.character(a$V1)
## starts=unlist(INDEXV(a$V1,a$V2,Genome,Step))
## ends=unlist(INDEXV(a$V1,a$V3,Genome,Step))
