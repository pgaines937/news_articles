
import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
from sklearn.model_selection import train_test_split
import csv
import datetime

def predict(x):
    if x == ".":
        return 0
    else:
        if float(x) >= 0:
            return 1
        else:
            return 0

df = pd.read_csv("c:/Users/kyungyong/Documents/Python Scripts/SML Project/final.csv")
df2 = pd.read_csv("c:/Users/kyungyong/Documents/Python Scripts/SML Project/DJIA.csv")
df2.rename(columns={'DATE': 'Date'}, inplace=True)

cols_to_keep = ['Class','Date', 'sentiment_polarity', 'sentiment_subjectivity', 'Positive', 'Negative', 'Neutral']
data = df[cols_to_keep]
data.drop_duplicates(subset=None, inplace=True)

data.Date = pd.to_datetime(data.Date)
df2.Date = pd.to_datetime(df2.Date)

df2.set_index(pd.DatetimeIndex(df2.Date), inplace=True)

df2 = df2.resample('D',fill_method='bfill')
df2.Date = df2.index.values
df2.Date = pd.to_datetime(df2.Date) - datetime.timedelta(days=1)

result_nq_mean = df.groupby('Date', as_index=False).mean()
result_nq_mean.Date = pd.to_datetime(result_nq_mean.Date)
result_nq_mean = result_nq_mean[cols_to_keep]


result_mean = df.groupby('Date', as_index=False).mean()
result_mean.Date = pd.to_datetime(result_mean.Date)


temp = pd.merge(result_mean, df2, on='Date')
temp.Class = temp.VALUE.map(lambda x: predict(x))
result_dj_mean = temp[cols_to_keep]

temp2 = pd.merge(data, df2, on='Date')
temp2.Class = temp2.VALUE.map(lambda x: predict(x))
result_dj = temp2[cols_to_keep]

data.to_csv("final_NASDAQ.csv", index=False)
result_nq_mean.to_csv("final_NASDAQ_Daily_Mean.csv", index=False)
result_dj.to_csv("final_DJIA.csv", index=False)
result_dj_mean.to_csv("final_DJIA_Daily_Mean.csv", index=False)
