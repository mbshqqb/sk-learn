import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import sklearn as sk

import os
os.chdir('E:\Programming\ZJ\IDEA\DataAnalysis\Python\sk-learn\data')
data=pd.read_csv('tianchi/coupon/ccf_offline_stage1_test_revised.csv')

test=data.apply(lambda X:X.apply(lambda x:np.NaN if x=='null' else x)).dropna().reset_index(drop=True)
test=test.astype({'User_id':'int64','Merchant_id':'int64','Coupon_id':'int64','Discount_rate':np.str,'Distance':np.int,'Date_received':np.int})

test['discount']=test['Discount_rate'].apply(lambda x: float(x) if x.find(':')==-1 else float(x.split(':')[1])/float(x.split(':')[0]))


test.drop()
print(test.head())