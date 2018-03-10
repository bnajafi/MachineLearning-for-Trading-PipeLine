# -*- coding: utf-8 -*-
import pandas as pd 
import os
import matplotlib.pyplot as plt
Repository_folder = "C:/Users/behzad/Dropbox/18 Eduameterial_Python_Finance/0 Udacity_machineLearning4Trading/MachineLearning-for-Trading-PipeLine"
os.chdir(Repository_folder)
companySymbol = "AAPL"
DataSet_path = "Data/"+companySymbol+".csv"
df_AAPL = pd.read_csv(DataSet_path, index_col = 0, parse_dates=True)
df_AAPL.head(10)
df_AAPL.tail(10)

df_AAPL["Close"].max()

df_AAPL["Volume"].mean()

plt.figure()
df_AAPL[["Close","Adj Close"]].plot()
plt.show()
plt.xlabel("time")
plt.legend()

start_date = "2010-01-22"
end_date = "2010-01-26"

dates = pd.date_range(start_date,end_date)
df1 = pd.DataFrame(index=dates)
df1.head()
companySymbol_2 = "SPY"
DF_SPY = pd.read_csv("/Data/{}.csv".format(companySymbol_2)