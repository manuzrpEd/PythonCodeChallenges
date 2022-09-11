import numpy as np
import pandas as pd

def solution(files):
    # files - any of available files, i.e:
    # files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
    #            "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
    #            "./data/twerche.csv", "./data/veeme.csv"]

    # write your solution here

    # return aggregated data from CSV files
    # file of each csv file is the name of company
    # date open max min close vol
    # return a list of length equal to files length
    # each list entry should have a  list of 2 dataframes
    # first df: highest volume by year, date and vol.
    # second df: highest close by year, date and close.
    lst = []
    for f in files:
        df = pd.read_csv(f)
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        df['year'] = df.index.year
        df = df.reset_index()
        vol = df.groupby(['year'])['vol'].max()
        vol = pd.merge(df, vol)
        vol = vol[['date', 'vol']]
        close = df.groupby(['year'])['close'].max()
        close = pd.merge(df, close, on=['year', 'close'])
        close = close[['date', 'close']]  
        lst.append([vol, close])
    return lst
    pass
