import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd


data = pd.read_csv('data.csv')
serie = data['values']

print(stats.kstest(serie, 'norm', (serie.mean(), serie.std()), N = len(serie)))

data.plot(kind='bar', xlabel='Number ', ylabel='T, C', title='Data')
data.plot.kde(xlabel='Number ', title='Data')

plt.show()