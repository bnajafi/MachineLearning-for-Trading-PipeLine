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
end_date = "2012-12-31"

dates = pd.date_range(start_date,end_date)
df1 = pd.DataFrame(index=dates)
df1.head()
companySymbol_2 = "SPY"
df_SPY = pd.read_csv("Data/{}.csv".format(companySymbol_2),index_col="Date",parse_dates=True,usecols=["Date","Adj Close"],na_values="nan")
df_SPY.rename(columns={"Adj Close":"SPY"},inplace=True)
df_SPY.head()

# NOw let's join 
df1=df1.join(df_SPY,how="inner" )

#df1.dropna()

#Now let's do the same with other datasets

CompanySymbols = ["GOOG", "IBM", "GLD"]
for companySymbol in CompanySymbols:
    df_company = pd.read_csv("Data/{}.csv".format(companySymbol),index_col="Date",parse_dates=True,usecols=["Date","Adj Close"],na_values="nan")
    df_company.rename(columns={"Adj Close":companySymbol},inplace=True)
    df1=df1.join(df_company,how="inner" )
plt.close("all")
plt.figure()
ax=df1.plot(title="Stock Prices",fontsize=12)  
ax.set_xlabel("Time")
ax.set_ylabel("Price")

#Let's normalize aevery Things
df1_normalized =(df1-df1.min())/(df1.max()-df1.min())

plt.close("all")
plt.figure()
ax=df1_normalized.plot(title="Stock Prices",fontsize=12)  
ax.set_xlabel("Time")
ax.set_ylabel("Price")

print df1.describe()

