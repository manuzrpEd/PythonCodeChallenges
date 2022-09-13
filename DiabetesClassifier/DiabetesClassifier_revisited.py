import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier

# train set
df_train = pd.read_csv(r'diabetes_train_info.csv')
df_train_analysis = pd.read_csv(r'diabetes_train_analysis.csv')
df_train = df_train.merge(df_train_analysis, left_on='id', right_on='id')

# preprocess
print('\n gender: \n', df_train['gender'].value_counts())
df_train['Female'] = np.where((df_train['gender']=='female') | (df_train['gender']=='f'),1,0)
df_train.drop('gender',axis=1,inplace=True)

print('\n age: \n', df_train['age'].value_counts())
df_train['age'] = df_train['age'].apply(lambda x: x/365 if len(str(x))>2 else x)

temp=pd.get_dummies(df_train['gluc'],drop_first=True,dummy_na=False).reset_index(drop=True)
temp=temp.add_prefix('gluc'+'_')
df_train.drop('gluc',axis=1,inplace=True)
df_train=pd.concat([df_train,temp],axis=1)

temp=pd.get_dummies(df_train['cholesterol'],drop_first=True,dummy_na=False).reset_index(drop=True)
temp=temp.add_prefix('cholesterol'+'_')
df_train.drop('cholesterol',axis=1,inplace=True)
df_train=pd.concat([df_train,temp],axis=1)

df_train['pressure_high']=df_train['pressure'].str.split('/').str[0].astype(int)
df_train['pressure_low']=df_train['pressure'].str.split('/').str[1].astype(int)
df_train.drop('pressure',axis=1,inplace=True)

df_train = df_train.dropna().reset_index()
df_train.drop('id',axis=1,inplace=True)
df_train.drop('index',axis=1,inplace=True)
# features and outcome variable
X=df_train.loc[:,df_train.columns!='diabetes']
y=df_train.diabetes

clf = LogisticRegression(random_state=0,fit_intercept=False,max_iter=2000000000000).fit(X,y)
print("\n Training Logistic Score :",round(clf.score(X,y),3))
#  Logistic Score : 0.973
df_train_pred = clf.predict(X)
# fit model no training data
model = XGBClassifier()
model.fit(X, y)
# make predictions for test data
y_pred = model.predict(X)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
#  XGBClassifier : 0.9995

# test set
df_test = pd.read_csv(r'diabetes_test_info.csv')
df_test_analysis = pd.read_csv(r'diabetes_test_analysis.csv')
df_test = df_test.merge(df_test_analysis, left_on='id', right_on='id')

# preprocess
print('\n gender: \n', df_test['gender'].value_counts())
df_test['Female'] = np.where((df_test['gender']=='female') | (df_test['gender']=='f'),1,0)
df_test.drop('gender',axis=1,inplace=True)

print('\n age: \n', df_test['age'].value_counts())
df_test['age'] = df_test['age'].apply(lambda x: x/365 if len(str(x))>2 else x)

temp=pd.get_dummies(df_test['gluc'],drop_first=True,dummy_na=False).reset_index(drop=True)
temp=temp.add_prefix('gluc'+'_')
df_test.drop('gluc',axis=1,inplace=True)
df_test=pd.concat([df_test,temp],axis=1)

temp=pd.get_dummies(df_test['cholesterol'],drop_first=True,dummy_na=False).reset_index(drop=True)
temp=temp.add_prefix('cholesterol'+'_')
df_test.drop('cholesterol',axis=1,inplace=True)
df_test=pd.concat([df_test,temp],axis=1)

df_test['pressure_high']=df_test['pressure'].str.split('/').str[0].astype(int)
df_test['pressure_low']=df_test['pressure'].str.split('/').str[1].astype(int)
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
#  Logistic Score : 0.973
df_test_pred = clf.predict(X)

# make predictions for test data
y_pred = model.predict(X)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
#  XGBClassifier : 0.9925

# fit model no training data
model = XGBClassifier()
model.fit(X, y)
# make predictions for test data
y_pred = model.predict(X)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))
#  XGBClassifier : 1.00



