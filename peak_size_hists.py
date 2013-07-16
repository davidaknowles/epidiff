import pylab, numpy

marks=["H3K27ac", "H3K4me1", "H3K4me3", "p300"]
cellsFile = open("cellList.txt")
cellsList = cellsFile.readlines()
cellsFile.close()
cellsList.append('ESC')

path = "/afs/cs.stanford.edu/u/davidknowles/scratch/p01project/QuEST_results/"
counter=1
for m in marks:
    for cell_raw in cellsList:
        cell=cell_raw.strip()
        pylab.subplot(len(marks),len(cellsList),counter)
        fn=path+"%s_%s.bed2.sorted"%(cell,m)
        f=open(fn)
        lengths=[] 
        for l in f:

            if l[0]=="c":
                a=l.split()
                length=long(a[2])-long(a[1])
                if length < 1e9: 
                    lengths.append(numpy.log10(length))
        print len(lengths)
        pylab.title(cell+" "+m)
        pylab.hist(lengths)
        xlim=pylab.gca().get_xlim() 
        pylab.xticks(xlim)
        counter=counter+1
        
pylab.show()