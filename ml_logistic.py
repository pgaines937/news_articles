
import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
from sklearn.model_selection import train_test_split
import csv

def predict(x):
    if x > 0.5:
        return 1
    else:
        return 0

def accuracy(x, y, z):
    if x == y:
        return z
    else:
        return 0

df = pd.read_csv("c:/Users/kyungyong/Documents/Python Scripts/final_DJIA.csv")
cols_to_keep = ['Class','sentiment_polarity', 'sentiment_subjectivity', 'Positive', 'Negative', 'Neutral']
data = df[cols_to_keep]
data['intercept'] = 1.0
train, test = train_test_split(data, test_size = 0.2)

train_cols = train.columns[2:7]
logit = sm.Logit(train['Class'], train[train_cols])
result = logit.fit()

test["predict"] = result.predict(test[train_cols])
test.predict = test.predict.map(lambda x: predict(x))

count = test.groupby(["Class", "predict"]).size().reset_index(name="Count")

print(count)
