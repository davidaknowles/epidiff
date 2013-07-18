from binReads import *
from mycompare import * 
import pickle
from pylab import * 

def load_data():
    with open("testdata.pickle","rb") as f: 
        data=pickle.load(f)
    return data

def test(data): 
    # data={}
    # print "1new"
    # data["b1"]=binReads("Fi1-GIIAX_Input_Sorted.NoBlack.tagAlign") 
    # print 2
    # data["s1"]=binReads("Fi1-GIIAX_p300_Sorted.NoBlack.tagAlign")
    # print 3
    # data["b2"]=binReads("Fi2-GIIAX_Input_Sorted.NoBlack.tagAlign") 
    # print 4
    # data["s2"]=binReads("Fi2-GIIAX_p300_Sorted.NoBlack.tagAlign") 

    #with open("testdata.pickle","wb") as f: 
    #    pickle.dump(data,f)

#    n=1000
    # s1={"chr1":data["s1"]["chr1"][0:n]}
    # b1={"chr1":data["b1"]["chr1"][0:n]}
    # s2={"chr1":data["s2"]["chr1"][0:n]}
    # b2={"chr1":data["b2"]["chr1"][0:n]}
    d2=compare2( data["s1"],data["b1"],data["s2"],data["b2"] )
#    d=compare( s1,b1,s2,b2 )
    # print d["chr1"][1:20]       
    # print d2["chr1"][1:20]
    n=10000
    chromo='chr1'

    data_keys=data.keys()

    for i in range(4):
        subplot(5,1,i+1)
        dk=data_keys[i]
        plot(data[dk][chromo][0:n])
        ylabel(dk)
    subplot(5,1,5)
    plot(d2[chromo][0:n])
    show() 
    return (data,d2)

def test_vs_background(data):
    
    
    for i in range(2):
        s='s%d'%(i+1)
        sample1=data[s]
        ba='b%d'%(i+1)
        background1=data[ba]
        chromo='chr1'
        (a,b)=compareToBackground( array( [sample1[chromo],background1[chromo]] ), .01, .01)
        subplot(7,1,1+i)
        ylabel(s)
        n=10000
        plot(  sample1[chromo][:n] )
        grid(1,which='major')
        subplot(7,1,3+i)
        plot(  background1[chromo][:n] )
        grid(1,which='major')
        ylabel(ba) 
        subplot(7,1,5+i)
        plot( (b-a)[:n] )
        ylabel('diff %d'%(i+1))
        grid(1,which='major')
    
    subplot(7,1,7)
    res=detectDifference2( array( [[data['s1'][chromo],data['b1'][chromo]],[data['s2'][chromo],data['b2'][chromo]]] ), pa=0.999)
    print(sum(res))
    plot( res[:n] )
    ylabel('global diff')
    show()

def varyPa(data):
    parange=array([ 0.01, 0.1, 0.5, 0.8, 0.9, .95, .99, .995, .999, .9999, .99999 ])
    chromo='chr1'
    res=detectDifferenceRangePa(array( [[data['s1'][chromo],data['b1'][chromo]],[data['s2'][chromo],data['b2'][chromo]]] ), parange)
    plot( parange, res ) 
    show()
    return (parange,res)

def varyPa2(data):
    parange=array([ 0.01, 0.1, 0.5, 0.8, 0.9, .95, .99, .995, .999, .9999, .99999 ])
    n=1000000
    chromo='chr1'
    res=detectDifferenceRangePa(array( [[data['s1'][chromo][:n],data['b1'][chromo][:n]],[data['s2'][chromo][:n],data['b2'][chromo][:n]]] ), parange)
    plot( parange, res ) 
    res2=detectDifferenceRangePa(array( [[data['s1'][chromo][:n],data['b1'][chromo][:n]],[data['s2']['chr2'][:n],data['b2']['chr2'][:n]]] ), parange)
    plot( parange, res2 ) 
    show()

if __name__=="__main__":
    test()
