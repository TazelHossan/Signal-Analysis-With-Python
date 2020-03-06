
import numpy as np
import pylab as plt
from math import pi
import random as gb
fm =4
fs =20*fm
am =2
t=np.linspace(0,2*np.pi ,50)
x =am*np.cos(2*fm*t)
plt.plot(t,x,'r')
#plt.show()
e= np.linspace(0,1,50)
eq= np.linspace(0, 1,50)
xq= np.linspace(0, 1,50)
#e=np.arange(500)
#eq=np.arange(500)
#xq=np.arange(500)
for n in range(1,len(x)-1):
    if n==1:
        e[n]=x[n]
        eq[n]=round(e[n])
        xq[n]=eq[n]
    else:
        e[n] =x[n]-xq[n-1]
        eq[n]=round(e[n])


#plt.plot(xq,'b')
#plt.show()
#xqr=np.arange(500)
xqr =np.linspace(0,1,50)
for n in range(1,len(x)-1):
    if n==1:
        xqr[n]=eq[n]
    else:
        xqr[n]=eq[n]+xqr[n-1]

plt.plot(t,xqr,'-y')
plt.show()