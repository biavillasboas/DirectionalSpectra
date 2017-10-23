import numpy as np

from getmem import GetMem
from plot_dirSpec import  plot_dirSpec

data = np.loadtxt('teste_spec.txt')

freq = data[:,0]
energy = data[:,2]
a1 = data[:,4]
b1 = data[:,5]
a2 = data[:,6]
b2 = data[:,7]

E = np.tile(energy, (360,1)).T
norm_mem= GetMem(a1,b1,a2,b2)

dirSpec = E*norm_mem
dirSpec = dirSpec.T

plot_dirSpec(dirSpec, freq, directions=None, vmin=0,filename=None)

