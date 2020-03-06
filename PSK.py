# Phase-shift keying (PSK)

import matplotlib as plt
import numpy as np
import pylab as pl
from math import pi
import random as gb

                                                           # Digital Input Data Of A Baseband Signal
v=[0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,1]

dim=100                                                    # 1D Array Dimension(1x100)

Vx=[]                                                      # Declare A List
Di=[]                                                      # Declare A List

for i in range(1,27):
    f=np.ones(dim)                                         # https://www.journaldev.com/32792/numpy-ones-in-python
    x=f*v[i]
    Vx=np.concatenate((Vx,x))

pl.subplot(4,1,1)                                          # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html
pl.title(r'$Data:0,0,1,1,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,1 $')
pl.plot(Vx,'y')

dim2=len(Vx)                                               # Same Dimension Of The Length Of The Baseband Signal (Vx)
t=np.linspace(0,5,dim2)
f1=4                                                       # Frecuency (Hz)
pl.subplot(4,1,2)                                          # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html
w1=2*np.pi*f1*t
y1=np.cos(w1)                                              # Create A cosine Signal
#pl.xlabel('x-axsis')
pl.ylabel('Amplitude(A)')
#pylab.plot(x, y2, 'm', label='cosine')
#pylab.legend(loc='upper right')
#pl.title(r'$s1(t)=A\cos(2 \pi f1)$')
pl.title(r'$s1(t)=A\cos(2 \pi f1)$')
pl.plot(t,y1, '-r', label='cosine')
pl.legend(loc='best')                                      # Plot The Signal (y1) in The Graph


f2=4                                                       # Frecuency (Hz)
pl.subplot(4,1,3)                                          # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html
#mult=(Vx*y1)
#pl.plot(t,mult)
#pl.show()
w2=2*np.pi*f2*t
y2=np.sin(w2)                                              # Create A sine Signal
                                                           # Plot The Signal (y2) in The Graph
pl.plot(t,y2 ,'m',label='sine')
pl.legend(loc='best')
pl.title(r'$s2(t)=A\sin(2 \pi f2)$')



pl.subplot(4,1,4)                                          # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html
res=((y2*Vx)-(y1*Vx) + (y1))
pl.plot(t,res,'g')                                         # Plot The Resultant Signal (res) in The Graph
pl.title(r'$S(t)=A\cos(2 \pi f1) + A\sin(2 \pi f2) $')
pl.xlabel('fig: PSK (Phase Shifting Key)')

pl.show()                                                  # Showing The Resulting 3 Signals In One Graph
