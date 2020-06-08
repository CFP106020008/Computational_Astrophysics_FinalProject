import numpy as np
import pandas as pd

P = np.loadtxt("star.txt")
r = (P[:,0]**2 + P[:,1]**2 + P[:,2]**2)**0.5*1e3

Radius = float(np.mean(r) + np.std(r)*8)

data = open('Dusty.ski','w+')
temp = open('Dusty.txt')

for i in temp:
    data.write(i.replace('5000',str(Radius)))

data.close()
temp.close()




