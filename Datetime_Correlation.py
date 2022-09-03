import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import quandl
import yfinance as yf
import scipy
import sklearn
print("Pandas version : ",pd.__version__)
print("")
print("Numpy version : ",np.__version__)
print("")
print("Scipy version : ",scipy.__version__)
print("")
print("sklearn version : ",scipy.__version__)
print("")
###
df=pd.read_csv('AirQualityUCI.csv',delimiter=';',decimal='.')
df=df[df['Date'].notna()]
#
df['datetime']=pd.to_datetime(df['Date'])
#
df.set_index('datetime', inplace=True)
df['day_of_month'] = df.index.day
df['month'] = df.index.month
df['hour'] = df['Time'].str[0:2]
df['year'] = df.index.year
df['day_of_week']  = df.index.weekday
df['week'] = df.index.week
#df=df.reset_index(drop=True)
caca=df[df.year == 2004]
caca=caca[caca.month == 5]
print("Max CO May 2004 : ",caca['CO(GT)'].max())
print("")
#
caca=df[['NOx(GT)','day_of_week','hour']]
caca=caca.sort_values(by=['NOx(GT)'],ascending=False)
print("NOx(GT) 10 highest values : ",caca[0:9])
print("")
print("Most common hour : ",caca['day_of_week'].mode())
print("")
print("Most common hour : ",caca['hour'].mode())
# caca=caca['Time'][0:1].astype(float)

###
df['CO(GT)'][:]=df['CO(GT)'].replace(',', '.')
df['CO(GT)']=float(df['CO(GT)'])
df['target']=df['CO(GT)'].shift(1)
correl=df.corr(method ='pearson') 
s = correl.unstack()
so = s.sort_values(kind="quicksort",ascending=False)
print("variables most correlated : ",so)

new=df[['PT08.','']]






