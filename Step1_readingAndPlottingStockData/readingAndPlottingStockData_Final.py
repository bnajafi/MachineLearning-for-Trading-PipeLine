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


def test_run():
    """ this function is called by the test Run"""
    Repository_folder = "C:/Users/behzad/Dropbox/18 Eduameterial_Python_Finance/0 Udacity_machineLearning4Trading/MachineLearning-for-Trading-PipeLine"
    os.chdir(Repository_folder)
    for CompanySymbol in ["AAPL", "IBM"]:
        print CompanySymbol, get_max_close(CompanySymbol)








if __name__ == "__main__":
    test_run()