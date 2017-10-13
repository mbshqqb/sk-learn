import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import sklearn as sk

import os
os.chdir('E:\Programming\ZJ\IDEA\DataAnalysis\Python\sk-learn\data')
data=pd.read_csv('tianchi/coupon/ccf_offline_stage1_train.csv')

train=data.apply(lambda X:X.apply(lambda x:np.NaN if x=='null' else x))
train=train[True^train['Coupon_id'].isnull()]
train=train.astype({'User_id':np.int,'Merchant_id':np.int,'Coupon_id':np.int,'Discount_rate':np.str,'Distance':np.float,'Date_received':np.float,'Date':np.float})

# train['Date']=train['Date'].fillna(20160101)

#哪些天会去
date_result=train.groupby('Date').size().reset_index(name='counts')
print(date_result[date_result['Date']==np.NaN])
plt.plot(date_result['Date'],date_result['counts'])
plt.show()
#哪些天收到的会去
# date_received_result=train.groupby('Date_received').size().reset_index(name='counts')
# plt.plot(date_received_result['Date_received'],date_received_result['counts'])
# plt.show()

#星期几会去
train['day']=(train['Date']+2)%7
# day_result=train.groupby('day').size().reset_index(name='counts')
# plt.plot(day_result['day'],day_result['counts'])
# plt.show()
#第几个月会去
train['month']=(train['Date']-20160000)/100
# month_result=train.groupby('month').size().reset_index(name='counts')
# plt.plot(month_result['month'],month_result['counts'])
# plt.show()

#每个月的第几天会去
train['day_of_month']=(train['Date']-20160000)%100
# day_of_month_result=train.groupby('day_of_month').size().reset_index(name='counts')
# plt.plot(day_of_month_result['day_of_month'],day_of_month_result['counts'])
# plt.show()
#每个月的第几天收到的会去
train['day_received_of_month']=(train['Date_received']-20160000)%100
# day_received_of_month_result=train.groupby('day_received_of_month').size().reset_index(name='counts')
# plt.plot(day_received_of_month_result['day_received_of_month'],day_received_of_month_result['counts'])
# plt.show()
#收到优惠券后几天会去
train['day_after']=train['Date']-train['Date_received']
# day_after_result=train.groupby('day_after').size().reset_index(name='counts')
# plt.plot(day_after_result['day_after'],day_after_result['counts'])
# plt.show()

#折扣率为多少会去
train['discount']=train['Discount_rate'].apply(lambda x: float(x) if x.find(':')==-1 else float(x.split(':')[1])/float(x.split(':')[0]))
# discount_result=train.groupby('discount').size().reset_index(name='counts')
# plt.plot(discount_result['discount'],discount_result['counts'])
# plt.show()


# gnb = sk.naive_bayes.GaussianNB()
#
# y_pred = gnb.fit(train.ix['Distance','day','month','day_of_month','day_received_of_month','day_received_of_month','day_received_of_month'], iris.target).predict(iris.data)