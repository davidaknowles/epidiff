from great_query import great_query
cells=["Ei1","Ci1","Fi1","Ni1"]
for cell in cells:
    fn=cell+"_enriched.bed"
    res=great_query(fn)
    res=res.ix[:,['Cell','Ontology','ID','Desc','BinomFdrQ']]
    res.to_csv(cell+"_go.csv")

