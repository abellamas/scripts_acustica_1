import matplotlib.pyplot as plt
import numpy as np

def change_section():
  return np.array([[1,0],[0,1]])

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



#frequency range to obtain values
f_range = np.arange(20, 20000, 1)


# ejecutar el tubo para cada frecuencia y guardar los datos en un array
# execute the tube for each frequency and save the data on an array

c=343 #sound propagation velocity
z=410 #characteristic impedance of the medium
r_tube=0.025 #radius tube in
r_chamber=0.061 #radius expansion chamber
l_in=0.15 #lenght inlet tube
l_chamber=0.0596 #lenght expansion chamber
l_conection=0.15 #lenght tube conection between mufflers
l_sb=0.30 #lenght side branch
l_out=0.15 #lenght outlet tube

T1_values = [] #matrix tube lenght l_in
T2_values = [] #matrix change section
T3_values = [] #matrix tube lenght l_chamber
T4_values = [] #matrix change section
T5_values = [] #matrix tube lenght l_conection
T6_values = [] #matrix side_branch
T7_values = [] #matrix tube lenght l_out
matrix_multiply = [] #contains all the resultants matrix
transmission_values = [] #contains all the TL values for each matrix

# tube_values = []
# side_b_values = []
# for f in f_range:
#   tube_values.append(tube(f=f,c=343,z=410,r=0.025,l=0.15))
#   side_b_values.append(side_branch(f=f,c=343,z=410,r_b=0.025,l=0.3))

for f in f_range:
  T1_values.append(tube(f,c,z,r_tube,l_in))
  # T2_values.append(change_section())
  T3_values.append(tube(f,c,z,r_chamber,l_chamber))
  # T4_values.append(change_section())
  T5_values.append(tube(f,c,z,r_tube,l_conection))
  T6_values.append(side_branch(f,c,z,r_tube,l_sb))
  T7_values.append(tube(f,c,z,r_tube,l_out)) 


for i in range(len(f_range)):
  # T_result = T1_values[i]@T2_values[i]@T3_values[i]@T4_values[i]@T5_values[i]@T6_values[i]@T7_values[i] #consider all the elements
  # T_result = T1_values[i]@T3_values[i]@T5_values[i]@T6_values[i]@T7_values[i] #delete the matrix of change section
  T_result = T3_values[i]@T5_values[i]@T6_values[i] #delete the matrix of inlet tube, change section and outlet tube
  matrix_multiply.append(T_result)

for j in range(len(f_range)):
  A,B,C,D=matrix_multiply[j][0,0], matrix_multiply[j][0,1], matrix_multiply[j][1,0], matrix_multiply[j][1,1]
  transmission_values.append(transmission_loss(A,B,C,D,0.025,410))



plt.plot(f_range,transmission_values)
plt.show()

