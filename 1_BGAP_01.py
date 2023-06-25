import numpy as np


CTAT = 1.6e-3
R1 = 3.6e3
k = 1.38e-23
q=1.6e-19
n=2
T=300
Id = 5e-6

R1 = (k*T/q)*np.log(n)/Id
R2 = R1*CTAT/(np.log(n)*(k/q))
print(R1)
print(R2)