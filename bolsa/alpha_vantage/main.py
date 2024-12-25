"""
 Alpha Vantage API Key

Welcome to Alpha Vantage! Your dedicated access key is: Z856YXA2J543AT2O. Please record this API key at a safe place for future data access.
"""



# from alpha_vantage.timeseries import TimeSeries
#
#
# api_key = "Z856YXA2J543AT2O"  # Obtén tu clave en alphavantage.co
# ts = TimeSeries(key=api_key, output_format="pandas")
#
# # Obtener datos intradía
# data, meta_data = ts.get_intraday(symbol="BTC-USD", interval="1min", outputsize="compact")  ## APPL
# print(data.head())



import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)