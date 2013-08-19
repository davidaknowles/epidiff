
mark="p300"
cell.line="EC2"

	a=read.table("all_p300.bed",sep="\t")
	a$V1=as.character(a$V1)
	load("hg18.RData") 
	source("ChIP.R")
	out.path="/srv/gs1/projects/snyder/imk1/P01Project/kdes/"
	Step=100
	width=10000
	Genome<-generate.genome.table(A,Step=Step)
	Genome$chr=as.character(Genome$chr)
	load(paste(out.path,"/",cell.line,"_",mark,".RData",sep=""))
	starts=INDEXV(a$V1,a$V2,Genome,Step)
	ends=INDEXV(a$V1,a$V3,Genome,Step)
	peaks=PEAKV(starts,ends,data.out) 
	save(peaks,file=paste(out.path,"/",cell.line,"_",mark,"_peaks.RData",sep=""))
