# loads aligned reads. So far only QuEST format implemented:" chromosome position strand"
# example of QuEST style file:
# chr3 128902087 -
# chr12 19302566 +
# chr12 118441111 +
# chr8 77752528 +
# chr1 41238553 -
# chr7 102553347 -
# chr9 86201564 -
# chr16 4292655 +
# chr3 32011700 +
# chr5 123146381 +

load.reads<-function(file,nrows=-1,Format="QuEST")
{
	if (!require(gdata)) stop("Package 'gdata' not found")
	if (Format=="QuEST")
	{
		sep<- " "
		a<-read.table(file, sep=" ", nrows=10)
		if (length(a)==1) {a<-read.table(file, sep="\t", nrows=10);sep <- "\t"} 
		if (nrows==-1){
		try(nrows<-strtoi(strsplit(trim(system(paste("wc -l",file),intern=TRUE))," ")[[1]][1]))}
		if (length(a)==2) read.table(file=file, sep=sep, nrows=nrows, comment.char="",colClasses=c("character","integer"))
		else read.table(file=file, sep=sep, nrows=nrows, comment.char="",colClasses=c("character","integer","character"))
	}
	else (stop(paste("type",type, "not implemented yet")))
	
}

# return lesser or greater of two values. Vectorized.
 lt<-function(a,b)ifelse(a<b,a,b)
 gt<-function(a,b)ifelse(a>b,a,b)

# generates a vector with kernel. require "source" which is a data frame with kernel parameters. Current version approximates 
# from fitted distributions to attain flexibility with step and bw.
# current kernel source data:
#       name          A1          S1          df1           A2         S2          df2             B
# 1  H3K4me1 0.010932725  1487.46729 1.3916991262 -0.007738903  231.80117 1.286531e+01 -0.0002425482
# 2  H3K4me3 0.324551000 60003.80000 0.0001328251 -0.001968600  162.15900 1.000000e+09 -0.0000611071
# 3  H3K27ac 0.004528261   714.77676 0.7985255861 -0.002052424  186.14208 1.403767e+01  0.0002117592
# 4 H3K27me3 0.041302186   490.37629 0.7018533668 -0.039278171  424.50323 4.834266e-01  0.0001403898
# 5     p300 0.025520167   155.37062 0.8803148582  0.008765301   41.04242 1.000000e+00  0.0003912825
# 6       TF 0.089167504    60.81358 2.2671812127  0.004570913 1022.75659 1.122180e+00  0.0003011282
# 

generate.kernel<-function(name, step, width=10000,bw=1000,asymmetric=FALSE,first=FALSE,source) # width is in bp. bw is SD for gauss
{
	width=round(width/2)
	x<-seq(-width,width,by=step)

	if (name=="gauss")
	{
		k<-dnorm(x,0,bw)
		k<-k-min(k)
		k<-k/sum(k)
		return(k)
	}
	else
	{
		a<- as.numeric(as.vector(source[source$name==name,2:8]))
		k<-a[1]*dt(x/a[2],a[3])+as.numeric(!first)*a[4]*dt(x/a[5],a[6])+a[7]
		k<-k-min(k)
		k<-k/sum(k)
		if(asymmetric) 	
		{
			L<-floor(length(k)/2)
			k[1:L]<- -k[1:L]
			k[L+1]<-0
		}
		return(k) 
	}
}


## Convolution implemented using fftw library

CONVOLVE <- function (x, y,  type = c("open","circular",  "filter")) 
{   if (!require (fftw)) stop("package fftw not found!")
    type <- match.arg(type)
    n <- length(x)
    ny <- length(y)
    Real <- is.numeric(x) && is.numeric(y)
    if (type == "circular") {
        if (ny != n) 
            stop("length mismatch in convolution")
    }
    else {
        n1 <- ny - 1
        x <- c(rep.int(0, n1), x)
        n <- length(y <- c(y, rep.int(0, n - 1)))
    }
	px<-planFFT(x)
	py<-planFFT(y)
    x <- IFFT(FFT(x,plan=px) * Conj( FFT(y,plan=py) ) )
    if (type == "filter") 
        (if (Real) 
            Re(x)
        else x)[-c(1L:n1, (n - n1 + 1L):n)]/n
    else (if (Real) 
        Re(x)
    else x)
}


# genome tables originate chromInfo.txt file deposited in UCSC genome browser
# Also header of SAM file contains the same information
# the table consists of chromosome name declaration and length in bp
# begining of hg19 genome table:
#  chr    length
# chr1 249250621
# chr2 243199373
# chr3 198022430
# chr4 191154276
# chr5 180915260
# chr6 171115067
# chr7 159138663
#
#function generate.genome.table generates following derivative:
# which contains cumulative counts of chromosome length in step lengths
#
#  chr    length      max       cum     start       end
# chr1 249250621 24925063         0         1  24925063
# chr2 243199373 24319938  24925063  24925064  49245001
# chr3 198022430 19802243  49245001  49245002  69047244
# chr4 191154276 19115428  69047244  69047245  88162672
# chr5 180915260 18091526  88162672  88162673 106254198
# chr6 171115067 17111507 106254198 106254199 123365705
# chr7 159138663 15913867 123365705 123365706 139279572

generate.genome.table<-function(Genome,Step)
{
	Genome$max<-ceiling(Genome$length/Step)
	Genome$cum<-0
	Genome$cum[2:length (Genome$chr)]<-cumsum(Genome$max[1:(length(Genome$chr)-1)])
	Genome$start<-Genome$cum+1
	Genome$end<-sum(Genome$max)
	Genome$end[1:(length(Genome$end)-1)]<-Genome$cum[2:(length(Genome$end))]
	return(Genome)
}

# calculate.ChIP is the main function
# control file contains instructions how to analyse aligned data
# it is in CSV format, example:
#  "kernel","genome","nrows","infile","outfile"
#  "TF","hg19",20425017,"~/Downloads/H9.pmNCC.Ap2a.q","/Volumes/DATA/H9.hg19.pmNCC.sh.Ap2a.out.wig"
#  "H3K27me3","hg19",19519128,"~/Downloads/H9.pmNCC.K27me3.q","/Volumes/DATA/H9.hg19.pmNCC.sh.K27me3.out.wig"
#  "H3K4me1","hg19",24587187,"~/Downloads/H9.pmNCC.K4me1.q","/Volumes/DATA/H9.hg19.pmNCC.sh.K4me1.out.wig"
#  "H3K4me3","hg19",22481793,"~/Downloads/H9.pmNCC.K4me3.q","/Volumes/DATA/H9.hg19.pmNCC.sh.K4me3.out.wig"
#  "TF","hg19",32153243,"~/Downloads/H9.pmNCC.NR2F1.q","/Volumes/DATA/H9.hg19.pmNCC.sh.NR2F1.out.wig"
#  "p300","hg19",15043340,"~/Downloads/H9.pmNCC.p300.q","/Volumes/DATA/H9.hg19.pmNCC.sh.p300.out.wig"

# number of rows is needed to overcome inefficient memory allocation in R. Providing it speeds things a lot.

# Step is interval in bp at which KDE is to be calculated
# witdh is the width of kernel in bp
# SHIFT is the peak shift value ( mean library fragment size), if set to -1 will trigger automated calculation

# the output is a vector of KDE values. The coordinates depend on the generated genome table. chr and position are not explicitly saved to save space.

calculate.ChIP<-function(control.file,Step=100, width=10000,SHIFT=-1)
{
	CF<-read.csv(file=control.file, stringsAsFactors=FALSE)
	I<-length (CF$infile)	
	SHIFT.PARAM<-SHIFT
for (s in 1:I)
	{
		
		load(paste("~/Genomics/ChIP.development/kernels functions and assemblies/",CF$genome[s],".RData", sep=""))
		Genome<-generate.genome.table(A,Step=Step)
		a<-load.reads(file=CF$infile[s],nrows=CF$nrows[s])
		if (SHIFT.PARAM<0)SHIFT<-calculate.shift(a,Genome)
		print(paste("Average library fragment size:",SHIFT,"\t",date()))
		if (SHIFT>0)a<-shift(a,SHIFT)
		KRN<-generate.kernel(name=CF$kernel[s],step=Step,width=width,source=kernels)
		print(paste("file:", CF$infile[s],date()))
		print(paste("Genome:",CF$genome[s],date()))
		print(paste("Kernel:",CF$kernel[s],date()))
		data.out<-ChIP(a,KRN,Step=Step,Genome=Genome)
		save(data.out, file=paste(CF$outfile[s],"RData",sep="."))
	}

}

#calculates peak shift. Slow. needs to be optimized and probably does not do the best job. Ignore warnings, some parts of genome will not produce meaningful shifts and are discarded
calculate.shift<-function(D,Genome)
{
	if (length(D)<3){print("No strand data. Shift calculation skipped");return(-1)} else
	{
		IND<-(1:length(Genome$chr))[Genome$length>5e6]
		SH<-rep(0,30)
		for (i in 1:30)
		{
			II<-sample(IND,1)
			CI<-Genome$chr[II]
			S<-round(runif(1,1,Genome$length[II]-2e6))
			m<-D$V2[D$V1==CI& D$V2>S & D$V2<S+1e6 & D$V3=="-"]
			p<-D$V2[D$V1==CI& D$V2>S & D$V2<S+1e6 & D$V3=="+"]
			M<-hist(m, breaks=seq(S,S+1e6,by=1),plot=FALSE)$counts
			P<-hist(p, breaks=seq(S,S+1e6,by=1),plot=FALSE)$counts
			C<-ccf(M,P,lag.max=300,plot=FALSE)
			try(SH[i]<-ksmooth(C$lag,C$acf,kernel="normal",bandwidth=100)$x[ksmooth(C$lag,C$acf,kernel="normal",bandwidth=100)$y==max(ksmooth(C$lag,C$acf,kernel="normal",bandwidth=100)$y)])
			 print(paste(i,SH[i],sep=":"))
		}
		return(median(SH[SH>40]))
		
	}
	
	
}

shift<-function(a,SHIFT)
{
	SHIFT<-SHIFT/2
	a$V2<-a$V2+(as.numeric(a$V3=="+")*2-1)*SHIFT
	return(a)

}

# main KDE routine. 
# reads mean data in Quest FORMAT
# Kernel is name of the kernel, as in kernel source table, e.g. "p300"
# Step is requested step size. 
# Genome is the output of generate.genome.table
# Max.chunk.size is size of pieces that are fed into FFT routine. Too large will create slowdowns.

ChIP<-function(Reads,Kernel,Step,Genome,Max.chunk.size=1048576)

{
	LK<-length(Kernel)
	LK<-floor(LK/2)
	OUT<-rep(1E-14,sum(ceiling(Genome$length/Step)))
	MAX.CHUNK<-2^floor(log2(Max.chunk.size))	#
#	MAX.CHUNK<-2^25
	for (k in 1:length(Genome$chr))
	{
		ch<-Genome$chr[k]
		print (paste("chromosome",ch, "\t",date()))
		b<-as.numeric(Reads$V2[Reads$V1==ch])
		b<-b[b>0 & b<= Genome$length[Genome$chr==ch]]
		x<-hist(b,breaks=seq(0,Step*ceiling(Genome$length[Genome$chr==ch]/Step),by=Step),plot=FALSE)$counts
		L<-length (x)
		NChunks<-ceiling(L/(MAX.CHUNK-4*LK))
		
		if(NChunks==1)
		{
			i=1
			#print (paste("chunk",i,"of",NChunks, "\t",date()))
			START<-1
			END<-L
			DATA<-x[START:END]	
			LL<-length(DATA)
			N<-2^ceiling(log2(length(DATA)))
			if (N>LL)DATA[(LL+1):N]<-0
			data.out<-CONVOLVE(DATA, Kernel, type="open")
			data.trim<-data.out[(LK+1):(END-START+(LK+1))]
			data.trim[abs(data.trim)<min(Kernel[Kernel!=0])/10]<-0
			OUT[Genome$start[k]:Genome$end[k]]<-data.trim
		}
		else 
		{
			TEMP.OUT<-c()
			for (i in 1:NChunks)
			{
				
				if (i==1)
					{
						#print (paste("chunk",i,"of",NChunks, "\t",date()))
						START<-1
						END<-i*(MAX.CHUNK-4*LK)+2*LK
						DATA<-x[START:END]	
						LL<-length(DATA)
						N<-2^ceiling(log2(length(DATA)))
						if (N>LL)DATA[(LL+1):N]<-0
						data.out<-CONVOLVE(DATA, Kernel, type="open")
						data.trim<-data.out[(LK+1):(END-START-2*LK+LK+1)]
						data.trim[abs(data.trim)<min(Kernel[Kernel!=0])/10]<-0
						TEMP.OUT <-data.trim
					}
					else if (i==NChunks)
					{
						#print (paste("chunk",i,"of",NChunks, "\t",date()))
						START<-(i-1)*(MAX.CHUNK-4*LK)+1-2*LK
						END<-L
						DATA<-x[START:END]	
						LL<-length(DATA)
						N<-2^ceiling(log2(LL))
						if (N>LL) DATA[(LL+1):N]<-0
						data.out<-CONVOLVE(DATA, Kernel, type="open")
						data.trim<-data.out[(3*LK+1):(END-START-4*LK+3*LK+1)]
						data.trim[abs(data.trim)<min(Kernel[Kernel!=0])/10]<-0
						TEMP.OUT <-c(TEMP.OUT ,data.trim)
					}
					else
					{
						#print (paste("chunk",i,"of",NChunks, "\t",date()))
						START<-(i-1)*(MAX.CHUNK-4*LK)+1-2*LK
						END<-i*(MAX.CHUNK-4*LK)+2*LK
						DATA<-x[START:END]	
						LL<-length(DATA)
						N<-2^ceiling(log2(LL))
						if (N>LL) DATA[(LL+1):N]<-0
						data.out<-CONVOLVE(DATA, Kernel, type="open")
						data.trim<-data.out[(3*LK+1):(END-START-4*LK+3*LK+1)]
						data.trim[abs(data.trim)<min(Kernel[Kernel!=0])/10]<-0
						TEMP.OUT <-c(TEMP.OUT ,data.trim)
					}
				}
			OUT[Genome$start[k]:Genome$end[k]]<-TEMP.OUT
		}
	}
	return(OUT)	
}



#some functions to work with the coordinates of the KDE vector

crange<-function(a,A){#this function takes UCSC coordinates string and converts it to vector of indexes, a is the UCSC string e.g "chr11:114,785,694-114,836,453" , A is the genome table
					b<-unlist((strsplit(a, ":|-")));#
					chr<-b[1];#
					start<-strtoi(paste(unlist(strsplit(b[2],",")), collapse=""));#
					end<-strtoi(paste(unlist(strsplit(b[3],",")), collapse=""));#
					return( (INDEX(chr,start,A)):(INDEX(chr,end,A))  )}

 CHR<-function(index, genome) genome$chr[findInterval(index,genome$cumulative)]; CHRV<-Vectorize(CHR, "index") # returns chromosome name given index/position in KDE data and genome data
 POS<-function(index, genome,step)round( step*(index - genome$cumulative[findInterval(index,genome$cumulative)])-step/2); POSV<-Vectorize(POS, "index") # returns position name given index/position in KDE data and genome data

INDEX<-function(chr,pos,genome) (ceiling(pos/10)+genome$cumulative[genome$chr==chr]);INDEXV<-Vectorize(INDEX, c("chr", "pos")) # returns index/position given chromosome position and genome

write.bed<-function(a, file)write.table(a, file=file, sep="\t", row.name=FALSE, col.names=FALSE, quote=FALSE)

PEAK<-function(start,end,DATA)max(DATA[start:end]); PEAKV<-Vectorize(PEAK,c("start", "end")) # returns peak height in a interval; start end are indexes, DATA is the KDE vector