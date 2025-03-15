import requests
import sqlite3
import schedule
import time
from datetime import datetime

# Configuración de la API del clima
API_KEY = "2c177eb16e77fa288cdee8bdbd153e14"
CITY = "Madrid"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def init_db():
    """Inicializa la base de datos SQLite y crea la tabla si no existe."""
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity INTEGER,
            description TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


def get_weather_data():
    """Obtiene datos del clima desde la API y los devuelve en un diccionario."""
    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"
    }
    print("Realizando solicitud a la API...")
    response = requests.get(BASE_URL, params=params)
    print("Estado de la respuesta API:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        print("Datos completos de la API:", data)
        weather_info = {
            "city": data.get("name"),
            "temperature": data.get("main", {}).get("temp"),
            "humidity": data.get("main", {}).get("humidity"),
            "description": data.get("weather", [{}])[0].get("description")
        }
        print("Datos procesados:", weather_info)
        return weather_info
    else:
        print("Error en la API:", response.text)
        return None


def save_weather_data(weather_info):
    """Guarda los datos del clima en la base de datos SQLite."""
    if weather_info and weather_info["city"] is not None:
        conn = sqlite3.connect("weather_data.db")
        cursor = conn.cursor()
        print("Guardando en DB:", weather_info)
        cursor.execute('''
            INSERT INTO weather (city, temperature, humidity, description)
            VALUES (?, ?, ?, ?)
        ''', (weather_info["city"], weather_info["temperature"], weather_info["humidity"], weather_info["description"]))
        conn.commit()
        conn.close()
        print(f"Datos guardados con éxito para {weather_info['city']}")
    else:
        print("Datos inválidos, no se guardarán en la base de datos.")


def fetch_and_store_weather():
    """Obtiene datos del clima y los almacena en la base de datos."""
    print("Obteniendo datos del clima...")
    weather_info = get_weather_data()
    print("Resultado de get_weather_data:", weather_info)
    if weather_info:
        save_weather_data(weather_info)
    else:
        print("No se obtuvieron datos válidos del clima.")


# Automatizar ejecución cada hora
schedule.every(1).hours.do(fetch_and_store_weather)

if __name__ == "__main__":
    init_db()
    fetch_and_store_weather()  # Ejecutar inmediatamente
    while True:
        schedule.run_pending()
        time.sleep(60)
