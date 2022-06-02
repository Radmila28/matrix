import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd


data = pd.read_csv('data.csv')

print(stats.kstest('norm', 'norm', N=3))
print(stats.kstest('norm', 'norm', N=500))

print(stats.kstest(data, 'norm', (data.mean(), data.std()), N=len(data)))

data.plot(kind='bar', xlabel='Number ', ylabel='T, C', title='Data')
data.plot.kde(xlabel='Number ', title='Data')

plt.show()
