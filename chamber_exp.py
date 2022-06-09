import matplotlib.pyplot as plt
import numpy as np

def chamber_exp(s_e,s_i,f,l,c):
  k = (2*np.pi*f)/c
  m=s_e/s_i
  return 10*np.log10(1+0.25*(m-1/m)**2*np.sin(k*l)**2) 

frequency_range = np.arange(20,5000,0.01)

plt.plot(frequency_range, chamber_exp(s_e=0.2, s_i=0.05, f=frequency_range, l=0.0596, c=343))

plt.legend(['Chamber Exp f=1438Hz'])
plt.grid()
plt.xlabel('Frecuencia [Hz]',fontsize=10)
plt.ylabel('TL [dB]',fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.ylim(0,10)
plt.xlim(20,4000)
plt.show()