import requests
import sqlite3
import schedule
import time
from datetime import datetime

#Configuracion de la base de datos
API_KEY = "2c177eb16e77fa288cdee8bdbd153e14"
CITY = "Madrid"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#Configuracion de la BD
def init_db():
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

#Funcion para obtener datos del clima
def get_weather_data():
    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        print("Datos procesados:", weather_info)  # Depuración
        return weather_info
    else:
        print("Error al obtener los datos del clima", response.status_code)
        return None

#Funcion para guardar datos en SQLite
def save_weather_data(weather_info):
    if weather_info:
        conn = sqlite3.connect("weather_data.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO weather (city, temperature, humidity, description)
            VALUES (?,?,?,?)
        ''', (weather_info["city"], weather_info["temperature"], weather_info["humidity"], weather_info["description"]))
        conn.commit()
        conn.close()
        print(f"Datos guardados: {weather_info}")

#Funcion principal
def fetch_and_store_weather():
    weather_info = get_weather_data()
    print("Resultado de get_weather_data:", weather_info)  # Depuración
    if weather_info:
        save_weather_data(weather_info)

#Automatizar ejecucion cada hora
schedule.every(1).hours.do(fetch_and_store_weather)

if __name__ == "__main__":
    init_db()
    fetch_and_store_weather()  # Ejecutar inmediatamente
    while True:
        schedule.run_pending()
        time.sleep(60)
