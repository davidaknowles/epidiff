from great_query import great_query
cells=["Ei1","Ci1","Fi1","Ni1"]
use_tomeks_enhancers=True
orig=False
subtract_background=False
#mark="H3K27me3"
mark="H3K27ac"
file_suffix="_".join(("enhancers",mark,"tomek" if (use_tomeks_enhancers) else "mine", "prog" if (orig) else "ipsc"))
#
for cell in cells:
    fn=cell+file_suffix+"_.RData"
    res=great_query(fn)
    res=res.ix[:,['Cell','Ontology','ID','Desc','BinomFdrQ']]
    res.to_csv(cell+file_suffix+"_go.csv")

