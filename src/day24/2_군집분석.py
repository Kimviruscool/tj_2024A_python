# 2_군집분석.py

import pandas as pd
import math

from numpy.ma.core import cumsum

retail_df = pd.read_excel('Online_Retail.xlsx')
# print(retail_df.head())

# print(retail_df.info())

retail_df = retail_df[retail_df['Quantity']>0]
retail_df = retail_df[retail_df['UnitPrice']>0]
retail_df = retail_df[retail_df['CustomerID'].notnull()]

retail_df['CustomerID'] = retail_df['CustomerID'].astype(int)
# print(retail_df.info())
# print(retail_df.isnull().sum())
# print(retail_df.shape)

retail_df.drop_duplicates(inplace = True)
# print(retail_df.shape)

pd.DataFrame([{'Product':len(retail_df['StockCode'].value_counts()),
               'Transaction':len(retail_df['InvoiceNo'].value_counts()),
               'Customer':len(retail_df['CustomerID'].value_counts())}],
             columns=['Product','Transaction','Customer'], index = ['counts'])

# print(retail_df['Country'].value_counts())

#주문 금액 컬럼 추가
retail_df['SaleAmount'] = retail_df['UnitPrice']*retail_df['Quantity']
# print(retail_df.head())

aggregations = {
    'InvoiceNo' : 'count',
    'SaleAmount' : 'sum',
    'InvoiceDate' : 'max'
}

customer_df = retail_df.groupby('CustomerID').agg(aggregations)
customer_df = customer_df.reset_index()
# print(customer_df.head())

customer_df = customer_df.rename(columns = {'InvoiceNo' : 'Freq', 'InvoiceDate':'ElapsedDays'})
# print(customer_df.head())

import datetime
customer_df['ElapsedDays'] = datetime.datetime(2011,12,10) - customer_df['ElapsedDays']
# print(customer_df.head())

customer_df['ElapsedDays']=customer_df['ElapsedDays'].apply(lambda x:x.days+1)
# print(customer_df.head())

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
ax.boxplot([customer_df['Freq'],customer_df['SaleAmount'],customer_df['ElapsedDays']], sym='bo')
plt.xticks([1,2,3],['Freq','SaleAmount','ElapsedDays'])
plt.show()

#데이터 분포조정
import numpy as np
customer_df['Freq_log'] = np.log1p(customer_df['Freq'])
customer_df['SaleAmount_log'] = np.log1p(customer_df['SaleAmount'])
customer_df['ElapsedDays_log'] = np.log1p(customer_df['ElapsedDays'])
print(customer_df.head())

fig, ax = plt.subplots()
ax.boxplot([customer_df['Freq_log'],customer_df['SaleAmount_log'],customer_df['ElapsedDays_log']], sym='bo')
plt.xticks([1,2,3],['Freq_log','SaleAmount_log','ElapsedDays_log'])
plt.show()

#분석 모델 구축
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
X_features = customer_df[['Freq_log','SaleAmount_log','ElapsedDays_log']].values

from sklearn.preprocessing import StandardScaler
X_features_scaled = StandardScaler().fit_transform(X_features)

#엘보 방법으로 클러스터 개수(k) 구하기
distortions = []

for i in range(1, 11):
    kmeans_i = KMeans(n_clusters=i,random_state=0)
    kmeans_i.fit(X_features_scaled)
    distortions.append(kmeans_i.inertia_)

plt.plot(range(1,11), distortions, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Distortion')
plt.show()

kmeans = KMeans(n_clusters=3, random_state=0) #모델 생성
Y_labels = kmeans.fit_predict(X_features_scaled)
customer_df['ClusterLabel'] = Y_labels
print(customer_df.head())