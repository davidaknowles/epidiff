path="~/P01Project/kdes/"
temp=as.character(read.table("cellList.txt")$V1)
cell.lines=c(temp,"ESC")
p300.peaks=read.table("all_p300.bed")
ra.all=matrix(nrow=46833,ncol=0)
for (cell.i in 1:length(cell.lines)){
    ai=cell.lines[cell.i]
    	load(paste(path,ai,"_H3K4me3_peaks.RData",sep=""))
	H3K4me3=peaks
	load(paste(path,ai,"_H3K4me1_peaks.RData",sep=""))
	H3K4me1=peaks
	ra=log(H3K4me3)-log(H3K4me1)
	ra[is.na(ra) & (H3K4me1==0.0) & (H3K4me3>0.0)]=2.0
	ra.all=cbind(ra.all,ra)

#    write.table(enriched,quote=F,col.names=F,row.names=F,file=paste(cells[[cell.i]][1],"_enriched.bed",sep=""))
}
ra.all[is.na(ra.all)]=0.0
my.promoters=apply(ra.all>1.15,1,any)
save(my.promoters,file="my.promoters.RData")
#pdf("promoter.pdf")
#hist(ra.all)
#dev.off()