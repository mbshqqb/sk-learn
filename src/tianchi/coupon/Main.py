import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import sklearn as sk
import sklearn.preprocessing as pc
import os
os.chdir('E:\Programming\ZJ\IDEA\DataAnalysis\Python\sk-learn\data')
data=pd.read_csv('tianchi/coupon/ccf_offline_stage1_train.csv')

train=data.apply(lambda X:X.apply(lambda x:np.NaN if x=='null' else x)).dropna()
train.dtype={'User_id':np.int,'Merchant_id':np.int,'Coupon_id':np.int,'Discount_rate':np.str,'Distance':np.int,'Date_received':np.int,'Date':np.int}

# le=pc.LabelEncoder()
# le.fit(train['Date'])
# train['Date']=le.transform(train['Date'])

# plt.hist(train['Date'])
# plt.show()