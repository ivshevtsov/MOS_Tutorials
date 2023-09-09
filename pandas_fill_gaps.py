import pandas as pd
import matplotlib.pyplot as plt

Home = 'DATA/pandas_fill'

str='X,Y,Z\n1,2.2,3\n2,2,3\n3,2,3\n4, ,3\n5, ,3'

file = open(f"{Home}/pandas_fill.txt", "w+")
file.write(str)
file.close()

pd_file = pd.read_csv(f'{Home}/pandas_fill.txt')

print(pd_file.columns.values)
print(pd_file.Y)

pd_file = pd_file.replace(to_replace=' ', value=0)
pd_file=pd_file.astype('float')

print(pd_file.Y)

plt.figure()
plt.plot(pd_file.X, pd_file.Y)

plt.show()