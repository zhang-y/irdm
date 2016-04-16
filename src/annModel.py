
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import FunctionTransformer
from sklearn import preprocessing
from sklearn.pipeline import FeatureUnion, make_pipeline
from datetime import datetime, timedelta
from keras.layers.core import Dense, Dropout, Activation
from keras.models import Sequential
from keras.optimizers import SGD


# In[2]:

loadtemp = pd.read_csv('./features/loadtemp_features_withsmoothtemp.csv')
target_dates = pd.date_range('2004-1-1', '2008-7-8', freq='1h')
target_dates = target_dates.delete(-1)
loadtemp.index = target_dates


# In[3]:

cols = loadtemp.columns
input_features = [i for i in cols if 'loadzone' not in i]
outputs = [i for i in cols if 'loadzone' in i]


# In[4]:

bk_date_start = ['2005-3-6 00:00:00', '2005-6-20 00:00:00', '2005-9-10 00:00:00', '2005-12-25 00:00:00', '2006-2-13 00:00:00', '2006-5-25 00:00:00', '2006-8-2 00:00:00', '2006-11-22 00:00:00']
bk_date_end = ['2005-3-12 23:00:00', '2005-6-26 23:00:00', '2005-9-16 23:00:00', '2005-12-31 23:00:00', '2006-2-19 23:00:00', '2006-5-31 23:00:00', '2006-8-8 23:00:00', '2006-11-28 23:00:00']
fk_date_start = '2008-6-23 06:00:00'
fk_date_end = '2008-6-30 05:00:00'
total_date_start = '2004-1-1 00:00:00'
total_date_end = '2008-7-7 23:00:00'
total_index = pd.date_range(total_date_start, total_date_end, freq='1h')
test_index = None
for i in range(len(bk_date_start)):
    s = bk_date_start[i]
    t = bk_date_end[i]
    if(i==0):
        test_index = pd.date_range(s, t, freq='1h')
    else:
        tmp_range = pd.date_range(s, t, freq='1h')
        test_index = test_index.union(tmp_range)
test_index = test_index.union(pd.date_range(fk_date_start, total_date_end, freq='1h'))
train_index = [i for i in total_index if i not in test_index]


# In[5]:

train = loadtemp.ix[train_index]
train = train.reset_index(drop=True)
test = loadtemp.ix[test_index]
test = test.reset_index(drop=True)


# In[6]:

def selectdata(df, selected_cols):
    df = df[selected_cols].copy()
    return df


# In[7]:

X = selectdata(train, input_features)
X_test = selectdata(test, input_features)
y = selectdata(train, outputs)
y_test = selectdata(test, outputs)


# In[8]:

X_scaled = preprocessing.scale(X)
X_test_scaled = preprocessing.scale(X_test)
y_scaled = preprocessing.scale(y)


# In[9]:

#input_dim = X_scaled.shape[1] # 31


# In[ ]:

for i in range(y.shape[1]):
    from keras.models import Sequential
    model = Sequential()

    model.add(Dense(output_dim=64, input_dim=31))
    model.add(Activation('tanh'))
    model.add(Dropout(0.2))
    model.add(Dense(output_dim=20, input_dim=64))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(output_dim=1, input_dim=20))
    model.add(Activation('linear'))

    model.compile(loss='mse',optimizer='sgd')

    model.fit(X_scaled, y_scaled[:,i])
    y_test_pred = model.predict(X_test_scaled)
    y_test[outputs[i]] = np.std(y[outputs[i]].values) * y_test_pred + np.mean(y[outputs[i]].values)


# In[ ]:

loadtemp.ix[test_index,outputs] = y_test.values


# In[ ]:

loadtemp.to_csv('./output/ann_keras_fit.csv', index=False)

