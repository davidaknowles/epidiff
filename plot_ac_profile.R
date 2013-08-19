path="~/P01Project/kdes/"
require(scales)
#png("Ei_vs_ESC.png",width=3000,height=3000)
#x11(width=1000,height=1000)
temp=as.character(read.table("cellList.txt")$V1)
cell.lines=c(temp,"ESC")
n=length(cell.lines)
par(mfrow=c(n,n))
print(n)
rqs=matrix(NA,ncol=n,nrow=n)
colnames(rqs)=cell.lines
rownames(rqs)=cell.lines
for (i in 1:n) for (j in 1:n)
{
	cell1=cell.lines[i]
	cell2=cell.lines[j]
	print(cell1)
	print(cell2)
	load(paste(path,cell1,"_H3K27ac_peaks.RData",sep=""))
	H3K27ac1=peaks/sum(peaks)
	load(paste(path,cell2,"_H3K27ac_peaks.RData",sep=""))
	H3K27ac2=peaks/sum(peaks)
	rqs[cell1,cell2]=summary(lm(H3K27ac1~H3K27ac2))$r.squared
#	plot( H3K27ac1, H3K27ac2 , xlab=cell1, ylab=cell2, main="H3K27ac profile", log="xy", col=alpha("black",.05) )
}
#dev.off()

save(rqs,file="rsquares.RData") 