# Passive Income Capstone Project
### Problem statement
Optimal investment for people with salary of  ฿15,000 - ฿30,000  ($400-$800), which are 40% of Thai population, that will yield passive income of ฿3,800/month ($100) in 3~5 years
- Bank Saving Interest:     ฿ 18M
- Corporate Bonds dividend: ฿ 1.5M
- Stocks dividend:          ฿ 912 K

Forex/Options trading: 
- initial portfolio: ฿ 3,800 
- 3% profit daily
- 186 days --> ฿ 912 K
- withdraw money and invest in stock for dividend

### Strategy backtesting
[Trima and Duoma Strategies](https://github.com/CoryMink/passive_income_capstone/blob/main/Tri_Duo_MA.ipynb) \
[Candlestick Patterns and Support/Resistance level](https://github.com/CoryMink/passive_income_capstone/blob/main/CandleStrategy.ipynb)
| Strategy  | Win Rate% | Return % | Number of Trades | Take Profit and Stop Loss |
| --------- | --------- | -------- | ---------------- |---|
| TriMA |  100%  |  13.78%  |  2  | 1000/500 |
| DuoMA  | 43.58%  | 22.60% | 39 | 1000/500 |
| Candle Pattern | 83.33% | 47.01% | 42 | 600/600 |

### Winrate optimization
[Winrate Optimization](https://github.com/CoryMink/passive_income_capstone/blob/main/WinRateOp.ipynb)
Run backtesting focusing on win rate only

RSI Indicator 
- overbought 70
- oversold 20
- period 22

EMA Inidcator
- Fast 10
- Medium 50
- Slow 190


### Machine Learning Model
[Machine Learning Models](https://github.com/CoryMink/passive_income_capstone/blob/main/PricePredict.ipynb)

Features: OHLC data, RSI(14), EMA(21,50,100) \
Target: Next day close price

| Regression Model  | Best Score | MSE | RMSE |
| ------------- | ------------- | -----| -----|
| Ridge   |  0.97905 | 0.00002 | 0.00397 |
| Linear   | 0.97875  | 0.00001 | 0.00377 |
| Random Forest | 0.94910 | 0.00001 | 0.00367 |
| Gradient Boosting | 0.94626 | 0.00001 | 0.00376 |
| KNN | 0.91113 |0.00004 | 0.00647 |
| SVR | 0.65204 | 0.00036 | 0.01893 |
| Lasso | -0.08354 | 0.00292 | 0.05402 |
| LSTM | | 0.00016 | 0.01272 |

### Check for data leak
[Dataleak Checking](https://github.com/CoryMink/passive_income_capstone/blob/main/daata_leak_or_not.ipynb)

Revisit the features and run on best model (Ridge Regression)
- Open,High,Low,RSI,3 Periods MA
- RSI, 3 Periods MA
- High, Low

Data leakage is unlikely

### Bonus:
[TP/SL senerio](https://github.com/CoryMink/passive_income_capstone/blob/main/tp_sl.ipynb)
You could make profit even if your win rate is 40% (even lower than coin flipping)

[prednow.py](https://github.com/CoryMink/passive_income_capstone/blob/main/prednow.py)
Symbol input with by the list of supported symbols \
Close Price Prediction in 15m,30m,60m,90m,1day,5day,1,week,1month
Support/Resistance levels in 180 days

[prediction](https://github.com/CoryMink/passive_income_capstone/blob/main/prediction.py)
Streammlit version of prednow.py
