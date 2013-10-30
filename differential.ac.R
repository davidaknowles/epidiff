use.tomeks.enhancers=T
orig=F
subtract.background=F
#mark="H3K27me3"
mark="H3K27ac"
file.suffix=paste("enhancers",mark,if (use.tomeks.enhancers) "tomek" else "mine",if (orig) "prog" else "ipsc",".RData",sep="_")
pvalue.file.name=paste("pvalues",file.suffix,sep="_")
if (use.tomeks.enhancers) {
    path="~/P01Project/ChIPseqData/tomek_enhancers/"
    p300.peaks=read.table("tomek_enhancers.bed")
    indices.to.keep=!logical(nrow(p300.peaks))
} else {
    path="~/P01Project/kdes/"
    p300.peaks=read.table("all_p300.bed")
    load("my.promoters.RData")
    indices.to.keep=!all.promoters
    p300.peaks=p300.peaks[indices.to.keep,]
}
temp=as.character(read.table("cellList.txt")$V1)
cell.lines=c(temp,"ESC")
if (orig){
    cells=list(c("EC","EC2"),c("CPC","CPC2"),c("FB1","FB2"),c("NSC"))
    extra=c("NSC","NSC2")
} else {
    cells=list(c("Ei1","Ei2"),c("Ci1","Ci2"),c("Fi1","Fi2"),c("Ni1"))
    extra=c("Ni1","Ni2")
}
res=list()
for (cell.i in 1:4){ # length(cells)){
    a=cells[[cell.i]]
    if (cell.i==4) a=extra
    b=list()
    for (j in 1:length(cells)) if (cell.i!=j) b=c(b,cells[[j]])
    A=list()
    for (ai in a) {
	load(paste(path,ai,"_",mark,"_peaks.RData",sep=""))
	A[[ai]]=peaks[indices.to.keep]
	if (subtract.background){
		load(paste(path,ai,"_",mark,"_background_peaks.RData",sep=""))
		A[[ai]]=A[[ai]]-peaks[indices.to.keep]
	}
    }
    B=list()
    for (bi in b) {
	load(paste(path,bi,"_",mark,"_peaks.RData",sep=""))
	B[[bi]]=peaks[indices.to.keep]
	if (subtract.background){
	   load(paste(path,bi,"_",mark,"_background_peaks.RData",sep=""))
	   B[[bi]]=B[[bi]]-peaks[indices.to.keep]
	}
    }
    print(a)
    print(b)
    res[[cell.i]]=numeric(length(A[[1]]))
    for (i in 1:length(A[[1]])) {
        ar=rep(NA,length(A))
	for (j in 1:length(A)) ar[j]=A[[j]][i]
    	br=rep(NA,length(B))
	for (j in 1:length(B)) br[j]=B[[j]][i]
    	res[[cell.i]][i]=t.test(ar,br,alternative="greater")[[3]]
    }
    p300.peaks$res=res[[cell.i]]
    s=p300.peaks[with(p300.peaks, order(res)),]
    #enriched=p300.peaks[res<0.01,]
    s$res=NULL
    enriched=s[1:100,]       
    write.table(enriched,quote=F,col.names=F,row.names=F,file=paste(cells[[cell.i]][1],file.suffix,sep=""))
}
save(res,file=pvalue.file.name)
#save(res,file="active_enhancer_pvalues_orig.RData")
#save(res,file="poised_pvalues_orig.RData")

