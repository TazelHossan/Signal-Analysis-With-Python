# Pulse Code Modulation (PCM)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

fsz = (7,5)                                            # Figure Size
fsz2 = (fsz[0],fsz[1]/2.0)                             # Half Height Of The Figure

                                                       # Initial Parameters
Fs = 8000                                              # Sampling Rate
fm = 1000                                              # Frequency Of Sinusoidal
tlen = 1.0                                             # Length in Seconds

                                                       # Generate Time Axis(x-axis)
t = np.arange(np.round(tlen*Fs))/float(Fs)

                                                       # Generate A sine wave (y-axis)
xt = np.sin(2*np.pi*fm*t)

                                                       # Print The First 12 Values Of x(t)
print('xt = {}'.format(xt[:12]))

                                                       # Create A Sinusoidal Graph
plt.figure(1, figsize=fsz)
plt.plot(t[:24], xt[:24], '-y')
plt.grid()                                             #Create The Grids In The Graph
plt.grid(which='major', axis='x', linestyle='-', color='k', linewidth=1.5)
plt.grid(which='major', axis='y', linestyle='-', color='k', linewidth=1.5)
                                                       # Create A Labeled Graph
plt.figure(2, figsize=fsz)
plt.plot(t[:24], xt[:24], '-y')
plt.plot(t[:24], xt[:24], 'or', label='xt values')
plt.ylabel('$x(t)$')
plt.xlabel('t [sec]')
strt2 = 'Sinusoidal Waveform $x(t)$'
strt2 = strt2 + ', $f_m={}$ Hz, $F_s={}$ Hz'.format(fm, Fs)
plt.title(strt2)
plt.legend()
plt.grid()                                             #Create The Grids In The Graph

plt.show()                                             #Show The PCM Graph
