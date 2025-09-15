import requests

api_url = "http://api.weatherstack.com/current?access_key=84878a38626394c5def7eeb2ac44e88c&query=New York"
# def fetch_data():
#     print("Fetching data from weatherstack API...")
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()
#         print("Data fetched successfully!")
#         # print(response.json())
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")
#         raise

# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-09-13 14:11', 'localtime_epoch': 1757772660, 'utc_offset': '-4.0'}, 'current': {'observation_time': '06:11 PM', 'temperature': 23, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '06:35 AM', 'sunset': '07:08 PM', 'moonrise': '10:36 PM', 'moonset': '01:49 PM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 66}, 'air_quality': {'co': '386.65', 'no2': '43.29', 'o3': '111', 'so2': '13.135', 'pm2_5': '26.64', 'pm10': '27.935', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 14, 'wind_degree': 164, 'wind_dir': 'SSE', 'pressure': 1020, 'precip': 0, 'humidity': 57, 'cloudcover': 0, 'feelslike': 25, 'uv_index': 6, 'visibility': 16, 'is_day': 'yes'}}