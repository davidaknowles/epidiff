path="~/P01Project/kdes/"
temp=as.character(read.table("cellList.txt")$V1)
cell.lines=c(temp,"ESC")
p300.peaks=read.table("all_p300.bed")
cells=list(c("Ei1","Ei2"),c("Ci1","Ci2"),c("Fi1","Fi2"),c("Ni1"))
subtract.background=F
load("my.promoters.RData")
indices.to.keep=!all.promoters
p300.peaks=p300.peaks[indices.to.keep,]
for (cell.i in 1:length(cells)){
    a=cells[[cell.i]]
    if (cell.i==4) a=c("Ni1","Ni2")
    b=list()
    for (j in 1:length(cells)) if (cell.i!=j) b=c(b,cells[[j]])
    A=list()
    for (ai in a) {
	load(paste(path,ai,"_H3K27ac_peaks.RData",sep=""))
	A[[ai]]=peaks[indices.to.keep]
	if (subtract.background){
		load(paste(path,ai,"_H3K27ac_background_peaks.RData",sep=""))
		A[[ai]]=A[[ai]]-peaks[indices.to.keep]
	}
    }
    B=list()
    for (bi in b) {
	load(paste(path,bi,"_H3K27ac_peaks.RData",sep=""))
	B[[bi]]=peaks[indices.to.keep]
	if (subtract.background){
	   load(paste(path,bi,"_H3K27ac_background_peaks.RData",sep=""))
	   B[[bi]]=B[[bi]]-peaks[indices.to.keep]
	}
    }
    print(a)
    print(b)
    res=numeric(length(A[[1]]))
    for (i in 1:length(A[[1]])) {
        ar=rep(NA,length(A))
	for (j in 1:length(A)) ar[j]=A[[j]][i]
    	br=rep(NA,length(B))
	for (j in 1:length(B)) br[j]=B[[j]][i]
    	res[i]=t.test(ar,br,alternative="greater")[[3]]
    }
    p300.peaks$res=res
    s=p300.peaks[with(p300.peaks, order(res)),]
    #enriched=p300.peaks[res<0.01,]
    s$res=NULL
    enriched=s[1:1000,]
    
    write.table(enriched,quote=F,col.names=F,row.names=F,file=paste(cells[[cell.i]][1],"_enhancers_enriched.bed",sep=""))
}
