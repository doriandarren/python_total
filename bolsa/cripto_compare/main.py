from api_client import fetch_data, save_to_database
from models import init_db


##url = "https://min-api.cryptocompare.com/data/top/mktcapfull?limit=10&tsym=USD"

api_key = '722d97b9dc79dbf9716a90ae7ab142aceda418bc1f7bab8e489b056d4b715c62'
url = f"https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD&api_key={api_key}"


# def search():
#     try:
#         response = requests.get(url)
#         response.raise_for_status() # Lanza una excepción si hay un error HTTP
#
#         data = response.json()
#
#         for item in data:
#             print(data)
#
#     except requests.exceptions.RequestException as e:
#         print(f"Error al realizar la solicitud {e}")




if __name__ == '__main__':
    init_db()

    symbol = "BTC"
    currency = "EUR"

    API_URL = f"https://min-api.cryptocompare.com/data/price?fsym={symbol}&tsyms={currency}"

    data = fetch_data(API_URL)


    if data:
        transformed_data = {
            "currency": currency,
            "symbol": symbol,
            "price": data.get(currency, 0.0)
        }

        save_to_database(transformed_data)
