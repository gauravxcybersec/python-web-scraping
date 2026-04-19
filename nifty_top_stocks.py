import yfinance as yf
import pandas as pd

# NIFTY 50 major stocks
nifty_stocks = [
    "RELIANCE.NS","TCS.NS","HDFCBANK.NS","ICICIBANK.NS","INFY.NS",
    "SBIN.NS","BHARTIARTL.NS","HINDUNILVR.NS","ITC.NS","KOTAKBANK.NS",
    "LT.NS","BAJFINANCE.NS","ASIANPAINT.NS","AXISBANK.NS","ULTRACEMCO.NS",
    "MARUTI.NS","SUNPHARMA.NS","WIPRO.NS","TECHM.NS","TITAN.NS"
]

data = []

for ticker in nifty_stocks:
    try:
        stock = yf.Ticker(ticker)
        info = stock.history(period="1d")

        if not info.empty:
            volume = info["Volume"].iloc[-1]
            price  = info["Close"].iloc[-1]
            data.append([ticker, price, volume])
    except:
        pass

df = pd.DataFrame(data, columns=["Ticker", "Price", "Volume"])
df = df.sort_values(by="Volume", ascending=False).head(10)

print("Top 10 Most Active NIFTY Stocks:")
print(df)
