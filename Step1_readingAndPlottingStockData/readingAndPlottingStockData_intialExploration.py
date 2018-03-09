# -*- coding: utf-8 -*-
import pandas as pd 
import os
Repository_folder = "C:/Users/behzad/Dropbox/18 Eduameterial_Python_Finance/0 Udacity_machineLearning4Trading/MachineLearning-for-Trading-PipeLine"
os.chdir(Repository_folder)
companySymbol = "AAPL"
DataSet_path = "Data/"+companySymbol+".csv"
df_AAPL = pd.read_csv(DataSet_path, index_col = 0, parse_dates=True)
df_AAPL.head(10)
df_AAPL.tail(10)

df_AAPL["Close"].max()

df_AAPL["Volume"].mean()
