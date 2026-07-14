import requests
from pymongo import MongoClient
from datetime import datetime

# Ganti dengan API key Anda
API_KEY = "6b8381ae84ef772c9e099daa23e73184"  # Dari notebook, ganti jika perlu

# Fungsi untuk fetch lat/lon
def get_lat_lon(city):
    BASE_URL = "http://api.openweathermap.org"
    URL = f"{BASE_URL}/geo/1.0/direct?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    data = response.json()
    if data:
        return data[0]['lat'], data[0]['lon'], data[0]['name']
    return None, None, None

# Fungsi untuk fetch forecast
def get_weather_forecast(lat, lon):
    BASE_URL = "http://api.openweathermap.org"
    FORECAST_URL = f"{BASE_URL}/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(FORECAST_URL)
    return response.json()

# Fungsi insert ke MongoDB
def insert_to_mongo(data, city_name):
    client = MongoClient('mongodb://mongodb:27017/')  # Gunakan service name 'mongodb' untuk Docker
    db = client['weather_db']  # Ganti nama DB jika perlu
    collection = db['forecast_collection']  # Ganti nama collection jika perlu

    # Proses data (transform: tambah city dan timestamp)
    for item in data['list']:
        item['city'] = city_name
        item['ingestion_time'] = datetime.now()
        collection.insert_one(item)

    print(f"Data for {city_name} ingested successfully!")

# Main ETL: Contoh untuk multiple cities (tambah kota lain jika perlu)
cities = ["malang", "jakarta", "surabaya"]  # Dari analisis notebook Anda (multiple cities)
for city in cities:
    lat, lon, city_name = get_lat_lon(city)
    if lat and lon:
        forecast_data = get_weather_forecast(lat, lon)
        insert_to_mongo(forecast_data, city_name)
    else:
        print(f"Failed to get coordinates for {city}")




