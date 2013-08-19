path="~/P01Project/kdes/"
cell.lines=read.table("cellList.txt")$V1
require(scales)
png("peak_types.png",width=1000,height=1000)
par(mfrow=c(4,4))
for (i in 1:length(cell.lines))
{
cell.line=cell.lines[i]
load(paste(path,cell.line,"_H3K4me1_peaks.RData",sep=""))
H3K4me1=peaks/sum(peaks)
load(paste(path,cell.line,"_H3K4me3_peaks.RData",sep=""))
H3K4me3=peaks/sum(peaks)
load(paste(path,cell.line,"_H3K27ac_peaks.RData",sep=""))
H3K27ac=peaks/sum(peaks)
load(paste(path,cell.line,"_H3K27me3_peaks.RData",sep=""))
H3K27me3=peaks/sum(peaks)
plot( log(H3K27ac)-log(H3K27me3) , log(H3K4me1)-log(H3K4me3), col=alpha("black",.05), main=cell.line)
}
dev.off()