# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 22:33:25 2015

From: http://danielhnyk.cz/predicting-sequences-vectors-keras-using-rnn-lstm/

@author: BearDeer
"""

from keras.models import Sequential  
from keras.layers.core import Dense, Activation  
from keras.layers.recurrent import LSTM
import pandas as pd
import numpy as np
import csv
from sklearn.metrics import roc_auc_score
from scipy import stats

def _load_data(data, n_prev = 20):
    """
    data should be pd.DataFrame()
    """

    docX, docY = [], []
#    for i in range(len(data)-n_prev):
#        docX.append(data.iloc[i:i+n_prev].as_matrix())
#        docY.append(data.iloc[i+n_prev].as_matrix())

    for s in data:
        for i in range(len(s) - n_prev):
            docX.append(np.transpose([s[i:i+n_prev]]))
            docY.append([s[i+n_prev]])
    alsX = np.array(docX)
    alsY = np.array(docY)

    return alsX, alsY

def train_test_split(df, test_size=0.2):
    """
    This just splits data to training and testing parts
    """
    ntrn = round(len(df) * (1 - test_size))

    X_train, y_train = _load_data(df[0:ntrn])
    X_test, y_test = _load_data(df[ntrn:])

    return (X_train, y_train), (X_test, y_test)

input_path = r'../data/naive_c2_q50_s4000_v0.csv'
input_file = open(input_path,'rb')
reader=csv.reader(input_file)
data_array=list(reader)
input_file.close()
data=np.array(data_array).astype('float')
print data.shape

in_out_neurons = 1
hidden_neurons = 100

(X_train, y_train), (X_test, y_test) = train_test_split(data)  # retrieve data

print X_train.shape
print y_train.shape
print X_test.shape
print y_test.shape

model = Sequential()
model.add(LSTM(hidden_neurons, input_dim=in_out_neurons, return_sequences=False))
model.add(Dense(in_out_neurons, input_dim=hidden_neurons))
model.add(Activation("tanh"))
model.compile(loss="mean_squared_error", optimizer="rmsprop")

model.fit(X_train, y_train, nb_epoch=10)

predicted = model.predict(X_test)
print 'done'

auc = 0
r_value = 0
rmse = np.sqrt(((predicted - y_test) ** 2).mean(axis=0))
auc = roc_auc_score(y_test, predicted)
#slope, intercept, r_value, p_value, std_err = stats.linregress(y_test,predicted)

print rmse, auc, "%.3f" % float(r_value**2)

# and maybe plot it
pd.DataFrame(predicted).to_csv("predicted.csv")
pd.DataFrame(y_test).to_csv("test_data.csv")
