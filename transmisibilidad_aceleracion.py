import matplotlib.pyplot as plt
import numpy as np

def trans(r,xi):
    m_maq = 0.985
    m_base = 0.15
    rel_masas = m_maq/m_base
    
    return 20*np.log10(rel_masas*np.sqrt((1+(2*xi*r)**2)/((1-r**2)**2+(2*xi*r)**2)))

# def w_0(k,m):
#     return np.sqrt(k/m)

# def xi(m,w_0,Ra):
#     return Ra/(2*m*w_0)

w_0 = 76.34
w = 281.48
xi =0.02679
r_range = np.arange(0,20,0.01)

plt.plot(r_range, trans(r_range,xi))

x,y=(w/w_0,trans(w/w_0,xi))

plt.scatter(x,y)
plt.text(x+.1, y+.9, (round(x,3),round(y,3)), fontsize=9)

plt.legend([f'xi={xi}'])
plt.grid()
plt.xlabel('r=w/w_0',fontsize=10)
plt.ylabel('Transmisibilidad [dB]',fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.ylim(-100,45)
plt.xlim(0,20)
plt.show()