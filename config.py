import os

# API Configuration
API_KEY = os.environ.get("OPENWEATHER_API_KEY", "your_actual_api_key_here")
BASE_URL = "https://api.openweathermap.org/data/2.5"

# Test Data
VALID_CITY = "London"
VALID_CITY_2 = "New York"
VALID_CITY_3 = "Tokyo"
INVALID_CITY = "InvalidCityXYZ123"

# Units
UNITS = "metric"