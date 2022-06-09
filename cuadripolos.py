import matplotlib.pyplot as plt
import numpy as np

def tube(f,c,z,r,l):
  s = np.pi*r**2
  k = (2*np.pi*f)/c
  A = np.cos(k*l)
  B = 1j*(z/s)*np.sin(k*l)
  C = 1j*(s/z)*np.sin(k*l)	
  return np.array([[A,B],[C,A]])

def side_branch(f,c,z,r_b,l):
  s_b = np.pi*r_b**2
  k = (2*np.pi*f)/c
  C = 1j*(s_b/z)*np.tan(k*l)
  return np.array([[1,0],[C,1]])
 

def multiply(f):
  T1 = tube(f=freq, c=343, z=410, r=0.1, l=0.0596)
  T2 = side_branch(f=freq, c=343, z=410, r_b=0.025, l=0.2998)
  matrix = np.matmul(T1,T2)
  return matrix

def transmission_loss(freq,r,z):

  matrix = multiply(freq)
  
  s = np.pi*r**2
  A,B,C,D = matrix[0,0],matrix[0,1],matrix[1,0],matrix[1,1]
  
  return 20*np.log10(0.5*np.abs(A+B*(s/z)+C*(z/s)+D))
  

f_range = np.arange(20, 40, 1)
  
# plt.plot(f_range,transmission_loss(tube(f_range,c=343, z=410,r=0.1,l=0.0596),r=0.025, z=410))
# plt.plot(f_range,transmission_loss(side_branch(f=f_range, c=343, z=410, r_b=0.025, l=0.3),r=0.025, z=410))
plt.plot(f_range,transmission_loss(f_range,r=0.025, z=410))
plt.show()