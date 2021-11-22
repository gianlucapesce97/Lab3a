import math
import random
import numpy as np
import matplotlib.pyplot as plt
import time


start_time=time.time()
ncx=[]
ncy=[]
nsx=[]
nsy=[]
nccounter=0
nscounter=0
N=1000
for i in range(N):
    x=np.random.uniform(-1,1)
    y=np.random.uniform(-1,1)
    d2=x**2+y**2
    if(d2<=1):
        nccounter+=1
        ncx.append(x)
        ncy.append(y)
    elif(d2>1):
        nscounter+=1
        nsx.append(x)
        nsy.append(y)

print("Numero dei punti dentro al cerchio: {0}\tNumero dei punti fuori dal cerchio: {1}".format(nccounter,nscounter))

pi=4*(nccounter/N)
print("Valore del pigreco pari a: %.5f"%pi)


plt.scatter(ncx,ncy,label="Inside",color='red',marker='.')
plt.scatter(nsx,nsy,label="Outside",color='blue',marker='.')
plt.legend()
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.savefig("CerchioMC")






print("Tempo di esecuzione pari a: ",time.time()-start_time)
