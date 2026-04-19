import yfinance as yf

ticker = input("Enter Stock Symbol (Example: AAPL or RELIANCE.NS): ")

stock = yf.Ticker(ticker)
data = stock.history(period="1d")

if data.empty:
    print("Invalid ticker or no data available.")
else:
    price = data["Close"].iloc[-1]
    print(f"Current price of {ticker}: {price}")
