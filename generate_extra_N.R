base.dir="~/P01Project/ChIPseqData/tomek_enhancers/"
marks=c("H3K27me3","H3K27ac")
cells=list(c("Ni1","Ni2"),c("NSC","NSC2"))
for (mark in marks)
    for (cell in cells){
        load(paste(base.dir,cell[1],"_",mark,"_peaks.RData",sep=""))
        non.zero.min=min(peaks[peaks>0])
        peaks[peaks==0]=non.zero.min
        a=log(peaks)
        a=a+0.2*rnorm(length(a))*sd(a)
        peaks=exp(a)
        save(peaks,file=paste(base.dir,cell[2],"_",mark,"_peaks.RData",sep=""))
#
        load(paste(base.dir,cell[1],"_",mark,"_background_peaks.RData",sep=""))
        non.zero.min=min(peaks[peaks>0])
        peaks[peaks==0]=non.zero.min
        a=log(peaks)
        a=a+0.2*rnorm(length(a))*sd(a)
        peaks=exp(a)
        save(peaks,file=paste(base.dir,cell[2],"_",mark,"_background_peaks.RData",sep=""))
    }
