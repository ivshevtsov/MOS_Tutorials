import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Folder = 'mirror'
Var_name='Id'

Discrepancy = pd.read_csv(f'random/{Folder}/Discrepancy_local.csv')
Hypercube =  pd.read_csv(f'random/{Folder}/Hypercube_local.csv')
Random =  pd.read_csv(f'random/{Folder}/Random_local.csv')

N = 10000

#plt.figure()
#plt.scatter(Discrepancy.Point[:N],Discrepancy.Vo[:N], label = 'Discrepancy')
#plt.legend()

#plt.figure()
#plt.hist(Discrepancy.Vo[:N], color='#99C1C2', label = 'Discrepancy')
#plt.legend()

dev_discrepancy = []
dev_hypercube = []
dev_random = []
NUM = []

for i in range(2,N):
    dev_discrepancy.append(np.std(Discrepancy[Var_name][:i]))
    dev_hypercube.append(np.std(Hypercube[Var_name][:i]))
    dev_random.append(np.std(Random[Var_name][:i]))
    NUM.append(i)


plt.figure()
plt.plot(NUM, dev_discrepancy, label='Discrepancy')
plt.plot(NUM, dev_hypercube, label = 'Hypercube')
plt.plot(NUM, dev_random, label='Random')
plt.axhline(y=dev_hypercube[-1], label='reference')
plt.legend()
plt.grid()





plt.show()
