import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# train set
df_train = pd.read_csv(r'diabetes_train_info.csv')
df_train_analysis = pd.read_csv(r'diabetes_train_analysis.csv')
df_train = df_train.merge(df_train_analysis, left_on='id', right_on='id')

# preprocess
df_train['Female'] = np.where(df_train['gender']=='female',1,0)
df_train.drop('gender',axis=1,inplace=True)

temp=pd.get_dummies(df_train['gluc'],drop_first=True,dummy_na=False).reset_index(drop=True)
temp=temp.add_prefix('gluc'+'_')
df_train.drop('gluc',axis=1,inplace=True)
df_train=pd.concat([df_train,temp],axis=1)

temp=pd.get_dummies(df_train['cholesterol'],drop_first=True,dummy_na=False).reset_index(drop=True)
temp=temp.add_prefix('cholesterol'+'_')
df_train.drop('cholesterol',axis=1,inplace=True)
df_train=pd.concat([df_train,temp],axis=1)

df_train['pressure_high']=df_train['pressure'].str.split('/').str[0]
df_train['pressure_low']=df_train['pressure'].str.split('/').str[1]
df_train.drop('pressure',axis=1,inplace=True)

df_train = df_train.dropna().reset_index()
df_train.drop('id',axis=1,inplace=True)
df_train.drop('index',axis=1,inplace=True)
# features and outcome variable
X=df_train.loc[:,df_train.columns!='diabetes']
y=df_train.diabetes

clf = LogisticRegression(random_state=0,fit_intercept=False,max_iter=2000000000000).fit(X,y)
print("\n Training Logistic Score :",round(clf.score(X,y),3))
#  Logistic Score : 0.874
df_train_pred = clf.predict(X)

# test set
df_test = pd.read_csv(r'diabetes_test_info.csv')
df_test_analysis = pd.read_csv(r'diabetes_test_analysis.csv')
df_test = df_test.merge(df_test_analysis, left_on='id', right_on='id')

# preprocess
df_test['Female'] = np.where(df_test['gender']=='female',1,0)
df_test.drop('gender',axis=1,inplace=True)

temp=pd.get_dummies(df_test['gluc'],drop_first=True,dummy_na=False).reset_index(drop=True)
temp=temp.add_prefix('gluc'+'_')
df_test.drop('gluc',axis=1,inplace=True)
df_test=pd.concat([df_test,temp],axis=1)

temp=pd.get_dummies(df_test['cholesterol'],drop_first=True,dummy_na=False).reset_index(drop=True)
temp=temp.add_prefix('cholesterol'+'_')
df_test.drop('cholesterol',axis=1,inplace=True)
df_test=pd.concat([df_test,temp],axis=1)

df_test['pressure_high']=df_test['pressure'].str.split('/').str[0]
df_test['pressure_low']=df_test['pressure'].str.split('/').str[1]
df_test.drop('pressure',axis=1,inplace=True)

# df_test.drop('Female',axis=1,inplace=True)

df_test = df_test.dropna().reset_index()
df_test.drop('id',axis=1,inplace=True)
df_test.drop('index',axis=1,inplace=True)
# features and outcome variable
X=df_test.loc[:,df_test.columns!='diabetes']
y=df_test.diabetes

clf = LogisticRegression(random_state=0,fit_intercept=False,max_iter=20000000000000000).fit(X,y)
print("\n Test Logistic Score :",round(clf.score(X,y),3))
df_test_pred = clf.predict(X)



