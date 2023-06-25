import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

Discrepancy = pd.read_csv('random_2/Discrepancy_global_local.csv')
Hypercube =  pd.read_csv('random_2/Hypercube_global_local.csv')
Random =  pd.read_csv('random_2/Random_global_local.csv')


N = 10000

plt.figure()
plt.scatter(Discrepancy.Point[:N],Discrepancy.Vo[:N], label = 'Discrepancy')
plt.legend()

plt.figure()
plt.hist(Discrepancy.Vo[:N], color='#99C1C2', label = 'Discrepancy')
plt.legend()

dev_discrepancy = []
dev_hypercube = []
dev_random = []
NUM = []

for i in range(2,N):
    dev_discrepancy.append(np.std(Discrepancy.Vo[:i]))
    dev_hypercube.append(np.std(Hypercube.Vo[:i]))
    dev_random.append(np.std(Random.Vo[:i]))
    NUM.append(i)


plt.figure()
plt.plot(NUM, dev_discrepancy, label='Discrepancy')
plt.plot(NUM, dev_hypercube, label = 'Hypercube')
plt.plot(NUM, dev_random, label='Random')
plt.axhline(y=dev_discrepancy[-1], label='reference')
plt.legend()
plt.grid()
plt.show()