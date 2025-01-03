import requests
from models import session, CryptoPrice


def fetch_data(api_url, params=None):
    """Realiza una solicitud GET a la API."""
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de la API: {e}")
        return None


def save_to_database(data):
    """Guarda los datos en la base de datos."""
    try:

        price_record = CryptoPrice(
            currency=data["currency"],
            symbol=data["symbol"],
            price=data["price"]
        )
        session.add(price_record)
        session.commit()
        print(f"Datos guardados: {data}")

    except Exception as e:
        print(f"Error al guardar datos en la base de datos: {e}")