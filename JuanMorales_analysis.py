import numpy as np
import matplotlib.pylab as plt

def normal_dist(x,mean,sigma):
	norm=(x-np.mean(x))/np.std(x)
	norm_final=(norm+mean)*sigma
	return norm_final

def get_fit(filename):
	data=np.loadtxt(filename, dtype=float)
	print "Promedio original: ", np.mean(data),"   Dsv.Std original: ",np.std(data)
	data2=normal_dist(data,0,1)
	print "Promedio nuevo: ", np.mean(data2),"   Dsv.Std nuevo: ",np.std(data2),'\n'
	plt.hist(data2)
	plt.savefig(filename+"Hist.png")
	
for j in range (1,4):
	get_fit("sample_1_"+str(10**j)+".txt")
	get_fit("sample_2_"+str(10**j)+".txt")
