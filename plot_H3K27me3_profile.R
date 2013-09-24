path="~/P01Project/kdes/"
require(scales)
png("poised_enhancers_only.png",width=3000,height=3000)
#x11(width=1000,height=1000)
temp=as.character(read.table("cellList.txt")$V1)
cell.lines=c(temp,"ESC")
n=length(cell.lines)
par(mfrow=c(n,n))
print(n)
rqs=matrix(NA,ncol=n,nrow=n)
colnames(rqs)=cell.lines
rownames(rqs)=cell.lines
load("my.promoters.RData") 
for (i in 1:n) for (j in 1:n)
{
	cell1=cell.lines[i]
	cell2=cell.lines[j]
	print(cell1)
	print(cell2)
	load(paste(path,cell1,"_H3K27me3_peaks.RData",sep=""))
	peaks=peaks[!all.promoters]
	H3K27ac1=peaks/sum(peaks)
	load(paste(path,cell2,"_H3K27me3_peaks.RData",sep=""))
	peaks=peaks[!all.promoters]
	H3K27ac2=peaks/sum(peaks)
	rqs[cell1,cell2]=summary(lm(H3K27ac1~H3K27ac2))$r.squared
	plot( H3K27ac1, H3K27ac2 , xlab=cell1, ylab=cell2, main="", log="xy", col=alpha("black",.05) )
}
dev.off()

save(rqs,file="rsquares_poised_enhancers.RData") 