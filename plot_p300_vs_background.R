path="~/P01Project/kdes/"

require(scales)
png("ac_vs_background.png",width=2000,height=2000)
#x11(width=1000,height=1000)
temp=as.character(read.table("cellList.txt")$V1)
cell.lines=c(temp,"ESC")
n=length(cell.lines)
par(mfrow=c(4,4))
print(n)
for (i in 1:n)
{
	cl=cell.lines[i]
	print(cl)
	load(paste(path,cl,"_H3K27ac_peaks.RData",sep=""))
	p300=peaks/sum(peaks)
	load(paste(path,cl,"_H3K27ac_background_peaks.RData",sep=""))
	bg=peaks/sum(peaks)
	plot( bg, p300, xlab="background", ylab="p300", main=cl, log="xy", col=alpha("black",.05) )
}
dev.off()