import numpy as np
import matplotlib.pylab as plt

def sample_1(N): 
	sample1=np.random.choice(a=[-10,-5,3,9],size=N,p=[0.1,0.4,0.2,0.3])
	return sample1

def sample_2(N):
	sample2=np.random.exponential(0.5,N)
	return sample2

def get_mean(sampling_fun,N,M):
	promedios=[]
	for i in range(0,M+1):
		promedios.append(np.mean(sampling_fun(N)))
	return np.array(promedios)

for j in range (1,4):
	np.savetxt("sample_1_"+str(10**j)+".txt",get_mean(sample_1,10**j,1000))
	np.savetxt("sample_2_"+str(10**j)+".txt",get_mean(sample_2,10**j,1000))

