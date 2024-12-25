import yfinance as yf


##ticker = "AAPL"

ticker = "BTC-USD"
data = yf.Ticker(ticker)


print(data.info)


current_price = data.history(period="1d")["Close"].iloc[-1]
print(f"Precio Actual de {ticker}: {current_price}")
