#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas    as pd
import numpy     as np
import yfinance  as yf
import pandas_ta as ta
import datetime  as dt
import time
from sklearn.model_selection  import train_test_split
from sklearn.linear_model     import LinearRegression


# In[10]:


def get_pred(sym):
    """
    sym = symbol based on Yahoo Finance
    get prediction of 
    """
    # Data request from Yahoo Finance
    tickers=sym
    enddate = dt.datetime.now()
    startdate = enddate - dt.timedelta(minutes=15000)
    lists1 = []
    for intervals in['15m','30m','60m','90m']:
        data = yf.download(tickers=tickers, start=startdate, end=enddate, interval=intervals,progress=False)
        data['NextClose'] = data['Close'].shift(-1)
        data.reset_index(inplace=True)
        data.dropna(inplace=True)
        X = data[['Open','High','Low']]
        y = data['NextClose']
        X_train,X_test,y_train,y_test = train_test_split(X,y,shuffle=False)
        lr = LinearRegression()
        lr.fit(X_train,y_train)
        y_pred = lr.predict(X_test)
        lists1.append(y_pred[-1])
        # ==============================================================
    tickers=sym
    enddate = dt.datetime.now()
    startdate = enddate - dt.timedelta(days=15000)
    lists2 = []
    for intervals in['1d','5d']:
        data = yf.download(tickers=tickers, start=startdate, end=enddate, interval=intervals,progress=False)
        data['NextClose'] = data['Close'].shift(-1)
        data.reset_index(inplace=True)
        data.dropna(inplace=True)
        X = data[['Open','High','Low']]
        y = data['NextClose']
        X_train,X_test,y_train,y_test = train_test_split(X,y,shuffle=False)
        lr = LinearRegression()
        lr.fit(X_train,y_train)
        y_pred = lr.predict(X_test)
        lists2.append(y_pred[-1])
        # ===============================================================
    tickers=sym
    enddate = dt.datetime.now()
    startdate = enddate - dt.timedelta(weeks=1000)
    lists3 = []
    for intervals in['1wk']:
        data = yf.download(tickers=tickers, start=startdate, end=enddate, interval=intervals,progress=False)
        data['NextClose'] = data['Close'].shift(-1)
        data.reset_index(inplace=True)
        data.dropna(inplace=True)
        X = data[['Open','High','Low']]
        y = data['NextClose']
        X_train,X_test,y_train,y_test = train_test_split(X,y,shuffle=False)
        lr = LinearRegression()
        lr.fit(X_train,y_train)
        y_pred = lr.predict(X_test)
        lists3.append(y_pred[-1])
        # ===================================================================
    tickers=sym
    enddate = dt.datetime.now()
    startdate = enddate - dt.timedelta(weeks=1000)
    lists4 = []
    for intervals in['1mo']:
        data = yf.download(tickers=tickers, start=startdate, end=enddate, interval=intervals,progress=False)
        data['NextClose'] = data['Close'].shift(-1)
        data.reset_index(inplace=True)
        data.dropna(inplace=True)
        X = data[['Open','High','Low']]
        y = data['NextClose']
        X_train,X_test,y_train,y_test = train_test_split(X,y,shuffle=False)
        lr = LinearRegression()
        lr.fit(X_train,y_train)
        y_pred = lr.predict(X_test)
        lists4.append(y_pred[-1])
    index = ['15m','30m','60m','90m','1d','5d','1wk','1mo']
    lists = lists1+lists2+lists3+lists4
    lists = pd.Series(lists).astype(float).round(5)
    lists.index = index
    print(lists)


# In[11]:


def sr_lv(sym):
    tickers=sym
    enddate = dt.datetime.now()
    startdate = enddate - dt.timedelta(days=180)
    df = yf.download(tickers=tickers, start=startdate, end=enddate, interval='1d',progress=False)
    df.drop(columns=['Adj Close','Volume'], inplace=True)
    df.columns = ['open','high','low','close']
    
    def support(df,l,n1,n2):
    
        for i in range(l-n1+1,l+1):
            if(df['low'][i]>df['low'][i-1]):
                return 0
        for i in range(l+1,l+n2+1):
            if(df['low'][i]<df['low'][i-1]):
                return 0
        return 1

    def resistance(df,l,n1,n2):
    
        for i in range(l-n1+1,l+1):
             if(df['high'][i]>df['high'][i-1]):
                return 0
        for i in range(l+1,l+n2+1):
            if(df['high'][i]<df['high'][i-1]):
                return 0
        return 1
    
    ss = []
    rr = []
    n1 = 2 
    n2 = 2 
    for row in range(5,len(df)-n2):
        if support(df,row,n1,n2):
            ss.append((row,df['low'][row],1))
        if resistance(df,row,n1,n2):
            rr.append((row,df['high'][row],2))
    
    sslist = [x[1] for x in ss if x[2]==1]
    rrlist = [x[1] for x in rr if x[2]==2]
    sslist.sort()
    rrlist.sort()

    for i in range(1,len(sslist)):
        if(i>=len(sslist)):
            break
        if abs(sslist[i]-sslist[i-1])<=0.005:
            sslist.pop(i)

    for i in range(1,len(rrlist)):
        if(i>=len(rrlist)):
            break
        if abs(rrlist[i]-rrlist[i-1])<=0.001:
            rrlist.pop(i)

    sr = rrlist+sslist
    for i in range(1,len(sr)):
        if(i>=len(sr)):
            break
        if abs(sr[i]-sr[i-1])<=0.01:
            sr.pop(i)
    
    print('SR level in 180 days')
    print(round(pd.Series(sr).sort_values(ascending=False),5))


# In[12]:


print('Supported Symbols: \n'
      '\n'
      'EURUSD=x, GBPUSD=x,USDJPY=x \n'
      'USDCHF=x, USDCAD=x, AUDUSD=x \n' 
      'NZDUSD=x \n'
      '\n'
      'Data refresh every 30 mins'
      '\n')
sym = input(f"Enter symbol: ")


# In[ ]:


while True:
    get_pred(sym)
    sr_lv(sym)
    print('-'*30)
    time.sleep(1800)

