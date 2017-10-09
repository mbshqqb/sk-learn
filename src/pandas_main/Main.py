import pandas
import matplotlib.pyplot as plt
df=pandas.read_csv('../../data/bank-data.csv')
# df.plot(kind='scatter',x='age',y='income',alpha=df['children'])
df['age'].hist()
# plt.plot(kind='bar',x=df['age'],y='income')
plt.show()