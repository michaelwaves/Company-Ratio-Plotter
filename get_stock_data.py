import yfinance as yf
import pandas as pd
import matplotlib

#input text file of tickers separated by spaces
with open('stocks.txt','r') as f: #must open read only for some reason
    stock_txt = f.read()

stocks = stock_txt.split()

'''
total_assets = []
total_debt = []
total_equity = []
revenue = []
operating_income = []'''


for stock in stocks:
    ticker = yf.Ticker(stock)
    df = ticker.financials #income statement pandas dataframe
    df_b = ticker.balance_sheet #balance sheet pandas dataframe
    #print(df['2021-12-31'])
    IS = df.loc[['Net Income','Operating Income','Total Revenue']]
    BS = df_b.loc[['Total Assets', 'Total Stockholder Equity','Total Liab']]
    dff = pd.concat([IS,BS], axis = 0)
    dff.loc['Asset Turnover'] = dff.loc['Total Revenue']/dff.loc['Total Assets']
    dff.loc['Return on Equity'] = dff.loc['Net Income']/dff.loc['Total Stockholder Equity']
    dff.loc['Operating Margin'] = dff.loc['Operating Income']/dff.loc['Total Revenue']
    dff.loc['Profit Margin'] = dff.loc['Net Income']/dff.loc['Total Assets']
    dff.loc['Debt to Equity'] = dff.loc['Total Liab']/dff.loc['Total Stockholder Equity']
    dff.loc['Debt to Total Assets'] = dff.loc['Total Liab']/dff.loc['Total Assets']
    dff = dff.drop(['Net Income','Operating Income','Total Revenue','Total Assets', 'Total Stockholder Equity','Total Liab'], axis = 0)
    print(dff)
    dff.plot(kind = 'line')
    
