import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


W = 5e-6
L = 550e-9
Vds = 100e-3

X_C = [0.660, 1.405]
Y_C = [14.453e-6, 137.88e-6]


K = (Y_C[1]-Y_C[0])/(X_C[1]-X_C[0])
b = Y_C[0] - X_C[0]*K


unCox = (K*L)/(W*Vds)
Vt = -(b*L)/(unCox*W*Vds)
Vt_2 = -(b*L)/(unCox*W*Vds*(1+0.5*Vds))
print(f'unCox={round(unCox*1e6,2)} u')
print(f'Vt1={round(Vt,2 )} V')
print(f'Vt2={round(Vt_2,2 )} V')

Veff = 1-Vt_2
Id = 0.5*unCox*(W/L)*Veff**2
gm = 2*Id/Veff
print(f'Calc Id ={Id}')
print(f'gm = {gm}')

NMOS = pd.read_csv('nmos_threshold.csv')
NMOS = NMOS.rename(columns={'Current_1 X':'Vgs', 'Current_1 Y':'Id'})
print(NMOS)



x = np.linspace(Vt,2,100)
y = K*x + b
plt.figure()
plt.plot(x, y*1e6)
plt.plot(NMOS.Vgs, NMOS.Id*1e6)
plt.grid()
plt.xlabel('Vgs, V')
plt.ylabel('Id, uA')

plt.show()