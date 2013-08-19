path="~/P01Project/kdes/"
temp=as.character(read.table("cellList.txt")$V1)
cell.lines=c(temp,"ESC")
p300.peaks=read.table("all_p300.bed")
cells=list(c("Ei1","Ei2"),c("Ci1","Ci2"),c("Fi1","Fi2"),c("Ni1"))
for (cell.i in 1:length(cells)){
    a=cells[[cell.i]]
    if (cell.i==4) a=c("Ni1","Ni2")
    b=list()
    for (j in 1:length(cells)) if (cell.i!=j) b=c(b,cells[[j]])
    A=list()
    for (ai in a) {
	load(paste(path,ai,"_H3K27ac_peaks.RData",sep=""))
	A[[ai]]=peaks
    }
    B=list()
    for (bi in b) {
	load(paste(path,bi,"_H3K27ac_peaks.RData",sep=""))
	B[[bi]]=peaks
    }
    res=numeric(length(A[[1]]))
    for (i in 1:length(A[[1]])) {
        ar=rep(NA,length(A))
	for (j in 1:length(A)) ar[j]=A[[j]][i]
    	br=rep(NA,length(B))
	for (j in 1:length(B)) br[j]=B[[j]][i]
    	res[i]=t.test(ar,br,alternative="greater")[[3]]
    }
    enriched=p300.peaks[res<0.05,]
    write.table(enriched,quote=F,col.names=F,row.names=F,file=paste(cells[[cell.i]][1],"_enriched.bed",sep=""))
}
