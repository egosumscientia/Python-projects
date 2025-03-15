# Weather Scraper Bot

## 📌 Descripción
Este proyecto es un bot de scraping que obtiene datos del clima desde la API de OpenWeather y los almacena en una base de datos SQLite.

## 🚀 Tecnologías Utilizadas
- **Python**
- **Requests** (para la conexión con la API)
- **SQLite** (para almacenar los datos)
- **Schedule** (para ejecutar automáticamente el script)

## 📂 Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/weather-scraper-bot.git
   cd weather-scraper-bot
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura tu API Key en `WeatherScraper.py`:
   ```python
   API_KEY = "TU_API_KEY"
   ```

## 📌 Uso
Para ejecutar el bot:
```bash
python WeatherScraper.py
```
El script se ejecutará automáticamente cada hora.

## ✅ Pruebas
Para ejecutar las pruebas unitarias:
```bash
python -m unittest test_weather_scraper.py
```

## 📊 Mejoras Futuras
- Crear una interfaz web con Flask.
- Añadir visualización de datos con Matplotlib.
- Soporte para múltiples ciudades.

¡Contribuciones y sugerencias son bienvenidas! 🎉

