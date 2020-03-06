# Frequency-division multiplexing (FDM)

import numpy as np
import pylab as pl
from scipy import signal
import matplotlib.pyplot as plt
from math import pi

t = np.linspace(0, 1,500)

Am1=1                                                     #Amplitude Of The First Signal (m1)
fm1=3                                                     #Frequency Of The First Signal(Hz)
m1=Am1*np.sin(2*np.pi*fm1*t)                              #Create The First Sinusoidal Signal (m1)
pl.figure(1)                                              #Mark The Signal(m3) as a Figure 1
pl.plot(t,m1,'r')                                         #Plot The First (m1) Signal
                                                          #Lable The First Signal (m1)
pl.xlabel('Absolute Frequincy')
pl.ylabel('DFT Values')
pl.title('Signal 1 with frequency 3Hz')
pl.show()                                                 # Showing The First Signal(m1)


Am2=2                                                     #Amplitude Of The Second Signal (m2)
fm2=4                                                     #Frequency Of The Second Signal(Hz)
m2=Am2*np.sin(2*np.pi*fm2*t )                             #Create The Second Sinusoidal Signal (m2)
pl.figure(2)                                              #Mark The Signal(m2) as a Figure 2
pl.plot(t,m2,'g')                                         #Plot The Second Signal(m2)
                                                          #Lable The Second Signal (m2)
pl.xlabel('Absolute Frequincy')
pl.ylabel('DFT Values')
pl.title('Signal 2 with frequency 4Hz')
pl.show()                                                 #Showing The Second Signal(m2)

Am3=0.18                                                  #Amplitude Of The Third Signal (m3)
fm3=5                                                     #Frequency Of The Third Signal(Hz)
m3=Am3*np.cos(2*np.pi*fm3*t)                              #Create The Third cosine Signal (m3)
pl.figure(3)                                              #Mark The Signal(m3) as a Figure 3
                                                          #Lable The Third Signal (m3)
pl.plot(t,m3,'b')                                         #Plot The Third Signal(m3)
                                                          #Lable The Third Signal (m3)
pl.xlabel('Absolute Frequincy')
pl.ylabel('DFT Values')
pl.title('Signal 3 with frequency 5Hz')
pl.show()                                                 # Showing The Third Signal(m3)

Ac1=2                                                     #Amplitude Of The First Carrier Signal (c1)
fc1=100                                                   #Frequency Of The First Carrier Signal(Hz)
c1=Ac1*np.sin(2*np.pi*fc1*t)                              #Create The First Carrier Sine Signal (c1)

Ac2=2                                                     #Amplitude Of The Second Carrier Signal (c2)
fc2=150                                                   #Frequency Of The Second Carrier Signal(Hz)
c2=Ac2*np.sin(2*np.pi*fc2*t)                              #Create The Second Carrier Sine Signal (c2)

Ac3=2                                                     #Amplitude Of The Third Carrier Signal (c3)
fc3=60                                                    #Frequency Of The Third Carrier Signal(Hz)
c3=Ac3*np.sin(2*np.pi*fc3*t)                              #Create The Third Carrier Sine Signal (c3)

x1=m1*c1 + m2*c2 + m3*c3                                  #Create The Composite Signal(x1) With
                                                          # Three Carrier Signals(m1*c1,m2*c2,m3*c3)


pl.figure(4)                                              #Mark The Signal(x1) as a Figure 4
pl.plot(t,x1 ,'c')                                        #Plot The Signal(x1)
                                                          #Lable The  Signal (x1)
pl.xlabel('Time')
pl.ylabel('Amplitude')
pl.title('Composite Signal of signals -1 ,2 ,3 ')
pl.show()                                                 #Showing The  Signal (x1)


x=m1 + m2 + m3                                            #Create The Composite Signal(x) With
                                                          # Three Baseband Signals(m1,m2,m3)
xn = x + np.random.randn(len(t)) * 0.08
pl.figure(5)                                              #Mark The Signal(xn) as a Figure 5
pl.plot(t,xn,'m')                                         #Plot The Signal(xn)
                                                          #Lable The  Signal (xn)
pl.xlabel('Absolute Frequincy')
pl.ylabel('DFT Values')
pl.title('Specturm of Composite Signal(signal-1 ,2 ,3)')
pl.show()                                                 #Showing The  Signal (xn)


pl.figure(6)                                              #Mark The Signal (m1*c1) as a Figure 6
pl.plot(t,m1*c1 ,'y')                                     #Plot The Signal(m1*c1)
                                                          #Lable The  Signal (m1*c1)
pl.xlabel('Absolute Frequincy')
pl.ylabel('DFT Values')
pl.title('Specturm of Signal 1 with 3Hz')
pl.show()                                                 #Showing The  Signal (m1*c1)


pl.figure(7)                                              #Mark The Signal (m2*c1) as a Figure 7
pl.plot(t,m2*c1 ,'k')                                     #Plot The Signal(m2*c1)
                                                          #Lable The  Signal (m2*c1)
pl.xlabel('Absolute Frequincy')
pl.ylabel('DFT Values')
pl.title('Specturm of Signal 2 with 4Hz')
pl.show()                                                 #Showing The  Signal (m2*c1)



pl.figure(8)                                              #Mark The Signal (m2*c1) as a Figure 8
pl.plot(t,m3*c1 ,'-r')
                                                          #Lable The  Signal (m3*c1)
pl.xlabel('Absolute Frequincy')
pl.ylabel('DFT Values')
pl.title('Specturm of Signal 3 with 5Hz')
pl.show()                                                 #Showing The  Signal (m3*c1)
#t = np.linspace(-1, 1, 201)
#x = (np.sin(2*np.pi*0.75*t*(1-t) + 2.1) + 0.1*np.sin(2*np.pi*1.25*t + 1) + 0.18*np.cos(2*np.pi*3.85*t))
#xn = x + np.random.randn(len(t)) * 0.08

#=======================================================================================================
#                              creating a filter for signal-1
#=======================================================================================================
b, a = signal.butter(3, 0.05)
zi = signal.lfilter_zi(b, a)
z, _ = signal.lfilter(b, a, xn, zi=zi*xn[0])
z2, _ = signal.lfilter(b, a, z, zi=zi*z[0])
y = signal.filtfilt(b, a, xn)
plt.figure(9)                                             #Mark The First Filtered Signal (m1) as a Figure 9
plt.plot(t, xn, 'b', alpha=0.75)                          #Plot The Signal(xn)
plt.plot(t, z, '-r', t, z2, 'r', t, y, 'k')               #Plot The Signal(z)
plt.legend(('noisy signal', 'lfilter, once', 'lfilter, twice','filtfilt'), loc='best')
plt.grid(True)                                            #Showing The Grides In The Graph
                                                          #Lable The  Signal
pl.xlabel('Absolute Frequincy')
pl.ylabel('DFT Values')
pl.title('Filtered Signal-1 with 3Hz')
plt.show()                                                #Showing The First Filtered Signal (m1)

#=======================================================================================================
#                                   creating a filter for signal-2
#=======================================================================================================
b, a = signal.butter(3, 0.07)
zi = signal.lfilter_zi(b, a)
z, _ = signal.lfilter(b, a, xn, zi=zi*xn[1])
z2, _ = signal.lfilter(b, a, z, zi=zi*z[1])
y = signal.filtfilt(b, a, xn)
plt.figure(10)                                            #Mark The Scecond Filtered Signal (m2) as a Figure 10
plt.plot(t, xn, 'b', alpha=0.75)                          #Plot The Signal(xn)
plt.plot(t, z, '-y', t, z2, 'r', t, y, 'k')               #Plot The Signal(z)
plt.legend(('noisy signal', 'lfilter, once', 'lfilter, twice','filtfilt'), loc='best')
plt.grid(True)                                            #Showing The Grides In The Graph
                                                          #Lable The Second Filtered Signal
pl.xlabel('Absolute Frequincy')
pl.ylabel('DFT Values')
pl.title('Filtered Signal-2 with 4Hz')
plt.show()                                                #Showing The Second Filtered Signal (m2)


#=======================================================================================================
#                                 creating a filter for signal-3
#=======================================================================================================
b, a = signal.butter(3, 0.09)
zi = signal.lfilter_zi(b, a)
z, _ = signal.lfilter(b, a, xn, zi=zi*xn[2])
z2, _ = signal.lfilter(b, a, z, zi=zi*z[2])
y = signal.filtfilt(b, a, xn)
plt.figure(11)                                           #Mark The Third Filtered Signal (m3) as a Figure 11
plt.plot(t, xn, 'b', alpha=0.75)                         #Plot The Signal(xn)
plt.plot(t, z, '-m', t, z2, 'r', t, y, 'k')              #Plot The Signal(z)
plt.legend(('noisy signal', 'lfilter, once', 'lfilter, twice','filtfilt'), loc='best')
plt.grid(True)                                           #Showing The Grides In The Graph
                                                         #Lable The Third Filtered Signal
pl.xlabel('Absolute Frequincy')
pl.ylabel('DFT Values')
pl.title('Filtered Signal-3 with 5Hz')
plt.show()                                               #Showing The Third Filtered Signal (m3)
