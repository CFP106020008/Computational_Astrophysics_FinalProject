import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import join

print("Please input the desired directory:")
path = input()
files = listdir(path)
files.sort()
files_abs = files
files_abs.sort()
for i in range(len(files)):
    files_abs[i] = join(path,files[i])

dash = '--'
line = '-'
#color = np.linspace(1000,5000,int(len(files)/2))
color = ['r',(0.8,0.52,0),(0.8,0.8,0),(0,0.8,0),'b',(111/255, 0, 255/255),(238/255,130/255,238/255),'k']

for i in range(0,len(files_abs)):
    Datas = np.loadtxt(files_abs[i])
    Datas[Datas==0] = 1e-60
    for rows in range(0,np.shape(Datas)[0]):
        if Datas[rows,0]>0.3:
            ROW = rows
            break
    tau = (np.log(Datas[:,2]/Datas[:,1]))/(np.log(Datas[ROW,2]/Datas[ROW,1]))
    LABEL = files[i].split('/')[-1]
    
    
    
    if i<0.5*len(files_abs):
        plt.plot(1/Datas[:,0],tau,color=color[i],linestyle='dashed',label=LABEL)
    else:
        plt.plot(1/Datas[:,0],tau,color=color[int(i-0.5*len(files_abs))],linestyle='solid',label=LABEL)

plt.legend(loc=2)
plt.title("Attenuation Curve \n (Normalized at {:4f} $\mu m$)".format(Datas[ROW,0]))
plt.xlabel(r'$1/\lambda$ $(\mu m^{-1})$')
plt.ylabel(r'$A/A_{3000 \AA}$')
plt.xlim([0.3,1/0.09])
plt.ylim([0,10])
plt.savefig(str(path+"_Attcur.png"),dpi=300)
#plt.show()
