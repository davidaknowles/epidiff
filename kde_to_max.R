run=function(mark,cell.line) 
{
	a=read.table("all_p300.bed",sep="\t") 
	load("hg18.RData") 
	source("ChIP.R")
	out.path="/srv/gs1/projects/snyder/imk1/P01Project/kdes/"
	Step=100
	width=10000
	Genome<-generate.genome.table(A,Step=Step)
	Genome$chr=as.character(Genome$chr)
	load(paste(out.path,"/",cell.line,"_",mark,"_background.RData",sep=""))
	a$V1=as.character(a$V1)
	starts=INDEXV(a$V1,a$V2,Genome,Step)
	ends=INDEXV(a$V1,a$V3,Genome,Step)
	peaks=PEAKV(starts,ends,data.out) 
	save(peaks,file=paste(out.path,"/",cell.line,"_",mark,"_background_peaks.RData",sep=""))
}

if (!interactive())
{
args=commandArgs(trailingOnly=T)
run(args[1],args[2])
}