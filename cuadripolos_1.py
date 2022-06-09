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
 



def transmission_loss(A,B,C,D,s,z):
  return 20*np.log10(0.5*np.abs(A+B*(s/z)+C*(z/s)+D))




f_range = np.arange(20, 40, 1)

# ejecutar el tubo para cada frecuencia y guardar los datos en un array
tube_values = []
side_b_values = []
matrix_multiply = []
transmission_values = []
for f in f_range:
  tube_values.append(tube(f=f,c=343,z=410,r=0.025,l=0.15))
  side_b_values.append(side_branch(f=f,c=343,z=410,r_b=0.025,l=0.3))


for i in range(len(f_range)):
  matrix_multiply.append(tube_values[i]@side_b_values[i])

for i in range(len(f_range)):
  A,B,C,D=matrix_multiply[i][0,0], matrix_multiply[i][0,1], matrix_multiply[i][1,0], matrix_multiply[i][1,1]
  transmission_values.append(transmission_loss(A,B,C,D,0.025,410))

print(transmission_values)

# plt.plot(f_range,transmission_loss(f_range,r=0.025, z=410))
# plt.show()

