import pandas as pd 
import os


def get_max_close(CompanySymbol):
    """this function simply returns the closing values of the stock indicated by the 
    company's symbol """
    df = pd.read_csv("data/{}.csv".format(CompanySymbol),index_col=0, parse_dates =True)
    return df["Close"].max()
    
def get_mean_volume(CompanySymbol):
    df = pd.read_csv("data/{}.csv".format(CompanySymbol),index_col=0, parse_dates =True)
    return df["Volume"].mean()

def symbol_to_path(symbol,folder_dir ="Data"):
   # return folder_dir+"/"+symbol+".csv"
    return os.path.join(folder_dir,"{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        
        df_new = pd.read_csv(symbol_to_path(symbol),index_col="Date",parse_dates=True,usecols=["Date","Adj Close"],na_values="nan")
        df_new.rename(columns={"Adj Close":symbol},inplace=True)

        df=df.join(df_new,how="inner")
        
    return df


def test_run():
    """ this function is called by the test Run"""
    Repository_folder = "C:/Users/behzad/Dropbox/18 Eduameterial_Python_Finance/0 Udacity_machineLearning4Trading/MachineLearning-for-Trading-PipeLine"
    os.chdir(Repository_folder)
    for CompanySymbol in ["AAPL", "IBM"]:
        print CompanySymbol, get_max_close(CompanySymbol)
   
    dates = pd.date_range('2010-01-22', '2010-01-26')
    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']
    # Get stock data
    df = get_data(symbols, dates)
    print df








if __name__ == "__main__":
    test_run()