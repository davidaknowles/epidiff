cells=c("Ei1","Ci1","Ni1","Fi1","EC","CPC","NSC","FB1","ESC")
cells.nice=c("Ei","Ci","Ni","Fi","EC","CPC","NSC","FB","H9")
names=c("endothelial iPSC","cardiac iPSC","neural iPSC","fibroblast iPSC","endothelial progenitor","cardiac progenitor","neural progenitor","fibroblast progenitor","H9")
#pdf(file="scatter.pdf",width=10,height=10)
png(file="~/Dropbox/shijun/scatter.png",width=1000,height=1000)
n.cells=length(cells) 
par(mfrow=c(n.cells+1,n.cells+1))
par(mar=c(1,1,1,1)*.1)
for (j in 1:(n.cells+1)) plot.new()
cex.factor=3
for (i in 1:n.cells) 
{
    plot.new()
    for (j in 1:n.cells)
    {
        cat(i)
        
        system(paste("python scatter_plot.py",cells[i],cells[j]))
        a=read.table("chip_to_plot.txt")
        colnames(a)=c(names[i],names[j])
        plot(sqrt(a),xaxt='n',yaxt='n',ann=F,col=rgb(0, 0, 1, .3))
        if (i==1) mtext(3,text=cells.nice[j],cex=cex.factor,padj=-.2)
        if (j==1) mtext(2,text=cells.nice[i],cex=cex.factor,padj=-.2)
    }

}
dev.off()
