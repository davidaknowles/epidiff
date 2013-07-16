from binReads import *
from mycompare import * 
import pickle

def test(): 
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
    with open("testdata.pickle","rb") as f: 
        data=pickle.load(f)
#    n=1000
    # s1={"chr1":data["s1"]["chr1"][0:n]}
    # b1={"chr1":data["b1"]["chr1"][0:n]}
    # s2={"chr1":data["s2"]["chr1"][0:n]}
    # b2={"chr1":data["b2"]["chr1"][0:n]}
    d2=compare2( data["s1"],data["b1"],data["s2"],data["b2"] )
#    d=compare( s1,b1,s2,b2 )
    # print d["chr1"][1:20]       
    # print d2["chr1"][1:20]
    return (data,d2)
if __name__=="__main__":
    test()
