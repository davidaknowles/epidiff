
require(ggplot2)
path="~/P01Project/kdes/"
temp=as.character(read.table("cellList.txt")$V1)
cell.lines=c(temp,"ESC")
p300.peaks=read.table("all_p300.bed")
cells=list(c("Ei1","Ei2"),c("Ci1","Ci2"),c("Fi1","Fi2"),c("Ni1"))
orig=list(c("EC","EC2"),c("CPC","CPC2"),c("FB1","FB2"),c("NSC"))
subtract.background=F
load("my.promoters.RData")
indices.to.keep=!all.promoters
p300.peaks=p300.peaks[indices.to.keep,]
#mark="H3K27me3"
#load("poised_pvalues_orig.RData")
mark="H3K27ac"
load("active_enhancer_pvalues.RData")
require(ggplot2)
use.log=T
first.time=T
count=0
for (o in orig){
    for (cell in o){
        load(paste(path,cell,"_",mark,"_peaks.RData",sep=""))
        if (use.log) peaks=log(peaks)
        if (first.time){
            average.val=peaks
        } else {
            average.val=average.val+peaks
            first.time=F
        }
        count=count+1
    }
}

average.val=average.val/count
for (cell.i in 1:length(cells)){
    p=res[[cell.i]]
    enriched=p<quantile(p,100/length(p))
    print(sum(enriched))
    pos=numeric(0)
    neg=numeric(0)
    for (o in orig[[cell.i]]){
    	load(paste(path,o,"_",mark,"_peaks.RData",sep=""))
        print(sum(peaks==0.0))
        if (use.log){
            peaks[peaks==0.0]=min(peaks[peaks!=0.0])
            log.peaks=log(peaks)
        } else {
            log.peaks=peaks
        }
        peaks=peaks-average.val
        pos=c(pos,log.peaks[indices.to.keep][enriched])
        neg=c(pos,log.peaks[indices.to.keep][!enriched])
    }
    print(t.test(pos,neg))
    pos=data.frame(kde=pos)
    neg=data.frame(kde=neg)
    pos$enrich="enriched"
    neg$enrich="background"
    pdf(file=paste("enrich",cells[[cell.i]][1],".pdf",sep=""))
    ggplot(rbind(pos,neg),aes(kde,fill=enrich))+geom_density(alpha=0.2)
    dev.off()
}

# ggplot(rbind(pos,neg),aes(y,fill=enrich))+geom_density(alpha=0.2,position="identity")
