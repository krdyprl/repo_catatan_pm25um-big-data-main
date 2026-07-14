#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OpenWeatherMap ETL Script
Fetch weather data from OpenWeatherMap API and store in MongoDB
"""

import requests
import pandas as pd
from pymongo import MongoClient
import os
import sys
from datetime import datetime

# Configuration
API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_API_KEY")
CITY = os.getenv("CITY", "surabaya")
MONGO_USERNAME = os.getenv("MONGO_USERNAME", "admin")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "password")
MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")

BASE_URL = "http://api.openweathermap.org"

def get_coordinates(city, api_key):
    """Get latitude and longitude from city name"""
    print(f"[{datetime.now()}] Fetching coordinates for {city}...")
    url = f"{BASE_URL}/geo/1.0/direct?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if not data:
            print(f"Error: City '{city}' not found")
            return None, None
        lat = data[0]['lat']
        lon = data[0]['lon']
        print(f"[{datetime.now()}] Coordinates found: LAT={lat}, LON={lon}")
        return lat, lon
    except requests.exceptions.RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return None, None

def get_forecast_data(lat, lon, api_key):
    """Fetch 5-day forecast data from OpenWeatherMap API"""
    print(f"[{datetime.now()}] Fetching forecast data...")
    url = f"{BASE_URL}/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"[{datetime.now()}] Forecast data fetched successfully")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return None

def connect_to_mongodb(username, password, host, port):
    """Connect to MongoDB and return client"""
    print(f"[{datetime.now()}] Connecting to MongoDB at {host}:{port}...")
    conn_str = f"mongodb://{username}:{password}@{host}:{port}/"
    try:
        client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)
        client.admin.command('ping')
        print(f"[{datetime.now()}] Connected to MongoDB successfully")
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

def insert_forecast_data(client, city, forecast_data):
    """Insert forecast data into MongoDB"""
    db = client["weather"]
    collection = db[city.lower()]
    
    try:
        # Insert all forecast records
        forecast_list = forecast_data['list']
        result = collection.insert_many(forecast_list)
        print(f"[{datetime.now()}] Inserted {len(result.inserted_ids)} documents into MongoDB")
        return collection
    except Exception as e:
        print(f"Error inserting data to MongoDB: {e}")
        return None

def analyze_weather_data(collection, city):
    """Analyze weather data and print statistics"""
    print(f"\n[{datetime.now()}] Analyzing weather data for {city}...")
    
    try:
        # Fetch data from MongoDB
        data = list(collection.find({}, {"_id": 0}))
        
        if not data:
            print("No data found in collection")
            return
        
        df = pd.DataFrame(data)
        
        # Extract temperature data
        df['temp'] = df['main'].apply(lambda x: x['temp'])
        avg_temp_kelvin = df['temp'].mean()
        avg_temp_celsius = avg_temp_kelvin - 273.15
        print(f"\n📊 Average temperature this week: {avg_temp_kelvin:.2f} K ({avg_temp_celsius:.2f} °C)")
        
        # Extract wind speed data
        df['wind_speed'] = df['wind'].apply(lambda x: x['speed'])
        max_wind = df['wind_speed'].max()
        print(f"💨 Max wind speed recorded: {max_wind:.2f} m/s")
        
        # Extract weather conditions
        df['weather_main'] = df['weather'].apply(lambda x: x[0]['main'])
        rain_count = (df['weather_main'] == "Rain").sum()
        total_count = len(df)
        print(f"🌧️  Rain occurred {rain_count} times out of {total_count} records")
        
        # Additional stats
        min_temp = df['temp'].min() - 273.15
        max_temp = df['temp'].max() - 273.15
        print(f"🌡️  Temperature range: {min_temp:.2f}°C to {max_temp:.2f}°C")
        
        print(f"\n✅ Analysis complete! Total records: {total_count}")
        
    except Exception as e:
        print(f"Error analyzing data: {e}")

def main():
    """Main ETL workflow"""
    print("=" * 60)
    print("OpenWeatherMap ETL Pipeline Started")
    print("=" * 60)
    
    # Validate API Key
    if API_KEY == "YOUR_API_KEY":
        print("❌ Error: Please set OPENWEATHER_API_KEY environment variable")
        sys.exit(1)
    
    # Step 1: Get coordinates
    lat, lon = get_coordinates(CITY, API_KEY)
    if lat is None or lon is None:
        print("❌ Failed to get coordinates")
        sys.exit(1)
    
    # Step 2: Fetch forecast data
    forecast_data = get_forecast_data(lat, lon, API_KEY)
    if forecast_data is None:
        print("❌ Failed to fetch forecast data")
        sys.exit(1)
    
    # Step 3: Connect to MongoDB
    client = connect_to_mongodb(MONGO_USERNAME, MONGO_PASSWORD, MONGO_HOST, MONGO_PORT)
    if client is None:
        print("❌ Failed to connect to MongoDB")
        sys.exit(1)
    
    # Step 4: Insert data
    collection = insert_forecast_data(client, CITY, forecast_data)
    if collection is None:
        print("❌ Failed to insert data")
        sys.exit(1)
    
    # Step 5: Analyze data
    analyze_weather_data(collection, CITY)
    
    print("\n" + "=" * 60)
    print("✅ ETL Pipeline Completed Successfully")
    print("=" * 60)

if __name__ == "__main__":
    main()