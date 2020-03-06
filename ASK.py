#Amplitude-shift keying (ASK)


import matplotlib as plt
import numpy as np
import pylab as pl
from math import pi
import random as gb
#plt.close('all')

v=[0,0,1,1,0,1,1,0,0,1,0]                             # Digital Input Data Of A Baseband Signal
dim=100                                               # 1D Array Dimension(1x100)
Vx=[]                                                 #Declare A List
for i in range(1,11):
    f=np.ones(dim)                                    # https://www.journaldev.com/32792/numpy-ones-in-python
    x=f*v[i]
    Vx=np.concatenate((Vx,x))

pl.subplot(3,1,1)                                     # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html
pl.title(r'$Data:0,0,1,1,0,1,1,0,0,1,0 $')
pl.plot(Vx ,'y')

dim2=len(Vx)                                          # Same Dimension Of The Length Of The Baseband Signal (Vx)
t=np.linspace(0,5,dim2)
f1=5                                                  # Frecuency
pl.subplot(3,1,2)                                     # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html
w1=2*np.pi*f1*t
y1=np.cos(w1)                                         # Create A cosine Signal
pl.title(r'$C(t)=A\cos(2 \pi f)$')
#pl.plot(t,y1, '-r', label='cosine')
#pl.legend(loc='upper right')
pl.plot(t,y1,'-r')

pl.subplot(3,1,3)                                     # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html
mult=(Vx*y1)                                          # Create A ASK Signal By Multiplying Baseband Signal(Vx) And A Carrier Signal(y1)
pl.title(r'$ASK$')
pl.plot(t,mult ,'g')
pl.xlabel('fig:Amplitude Shift Keying(ASK)')
pl.show()                                             # Showing The Resulting 3 Signals In One Graph