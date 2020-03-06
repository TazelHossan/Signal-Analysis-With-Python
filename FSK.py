# Frequency-shift keying (FSK)

import matplotlib as plt
import numpy as np
import pylab as pl
from math import pi
import random as gb

v=[0,0,1,1,0,1,1,0,0,1,0]                              # Digital Input Data Of A Baseband Signal

dim=100                                                # 1D Array Dimension(1x100)

Vx=[]                                                  # Declare A List

for i in range(1,11):
    f=np.ones(dim)                                     # https://www.journaldev.com/32792/numpy-ones-in-python
    x=f*v[i]
    Vx=np.concatenate((Vx,x))

pl.subplot(4,1,1)                                      # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html
pl.title(r'$Data:0,0,1,1,0,1,1,0,0,1,0 $')
pl.plot(Vx,'y')


dim2=len(Vx)                                           # Same Dimension Of The Length Of The Baseband Signal (Vx)
t=np.linspace(0,5,dim2)
f1=5                                                   # Frecuency (Hz)
pl.subplot(4,1,2)                                      # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html
w1=2*np.pi*f1*t
y1=np.cos(w1)                                          # Create A cosine Signal
#pl.xlabel('x-axsis')
#pl.ylabel('y-axsis')
#pylab.plot(x, y2, 'm', label='cosine')
#pylab.legend(loc='upper right')
pl.title(r'$s1(t)=A\cos(2 \pi f1)$')
pl.plot(t,y1, '-r', label='cosine')
pl.legend(loc='best')

pl.subplot(4,1,3)                                      # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html
#mult=(Vx*y1)
#pl.plot(t,mult)
#pl.show()
f2=20                                                  # Frecuency(Hz)
w2=2*np.pi*f2*t
y2=np.cos(w2)                                          # Create A cosine Signal
pl.plot(t,y2 ,'m',label='cosine')
pl.legend(loc='best')
pl.title(r'$s2(t)=A\cos(2 \pi f2)$')
#pl.plot(x, y2, 'm', label='cosine')

pl.subplot(4,1,4)                                      # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html

Di=[]                                                  # Declare A List

for i in range(0,dim2):

    if Vx[i]==0:
        x=np.array([y1[i]])
        Di=np.concatenate((Di,x))
    else:
        y=np.array([y2[i]])
        Di=np.concatenate((Di,y))

pl.title(r'$S(t)=A\cos(2 \pi f1) + A\cos(2 \pi f2) $')
pl.xlabel('fig: FSK (Frequincy Shifting Key)')
pl.plot(t,Di ,'b')

pl.show()                                             # Showing The Resulting 3 Signals In One Graph