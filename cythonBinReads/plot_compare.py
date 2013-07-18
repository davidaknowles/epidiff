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
