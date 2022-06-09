import matplotlib.pyplot as plt
import numpy as np

def side_branch(s,s_d,f,l,c):
  k = (2*np.pi*f)/c
  return 10*np.log10(1+((s_d/(2*s))*np.tan(k*l) )**2) 

frequency_range = np.arange(20,20000,0.01)

plt.plot(frequency_range, side_branch(s=0.050,s_d=0.050,f=frequency_range,l=0.2998,c=343))

plt.legend(['side branch f=286Hz'])
plt.grid()
plt.xlabel('Frecuencia [Hz]',fontsize=10)
plt.ylabel('TL [dB]',fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.ylim(0,100)
plt.xlim(20,4000)
plt.show()