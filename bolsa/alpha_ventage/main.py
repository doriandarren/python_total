import requests




api_key = 'S8OFIORUACQS1M45'
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=EUR&apikey={api_key}"


def search():
    try:
        response = requests.get(url)
        response.raise_for_status() # Lanza una excepción si hay un error HTTP

        data = response.json()

        ##print(data)

        # Extraer el precio actual del Bitcoin
        tasa_cambio = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

        print(tasa_cambio)


        # return float(tasa_cambio)

        # for item in data:
        #     print(data)

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud {e}")



if __name__ == '__main__':
    search()