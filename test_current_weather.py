import requests
from config import API_KEY, BASE_URL, VALID_CITY, VALID_CITY_2, VALID_CITY_3, UNITS

class TestCurrentWeather:

    # Test 1 - Get current weather for a valid city
    def test_get_weather_london(self):
        response = requests.get(
            f"{BASE_URL}/weather",
            params={
                "q": VALID_CITY,
                "appid": API_KEY,
                "units": UNITS
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "London"
        assert "main" in data
        assert "temp" in data["main"]
        assert "humidity" in data["main"]
        assert "weather" in data

    # Test 2 - Verify temperature is a real number
    def test_temperature_is_valid(self):
        response = requests.get(
            f"{BASE_URL}/weather",
            params={
                "q": VALID_CITY,
                "appid": API_KEY,
                "units": UNITS
            }
        )
        assert response.status_code == 200
        data = response.json()
        temp = data["main"]["temp"]
        assert isinstance(temp, (int, float))
        assert -100 < temp < 100  # Reasonable temperature range

    # Test 3 - Get weather for multiple cities
    def test_get_weather_multiple_cities(self):
        cities = [VALID_CITY, VALID_CITY_2, VALID_CITY_3]
        for city in cities:
            response = requests.get(
                f"{BASE_URL}/weather",
                params={
                    "q": city,
                    "appid": API_KEY,
                    "units": UNITS
                }
            )
            assert response.status_code == 200
            data = response.json()
            assert "main" in data
            assert "temp" in data["main"]

    # Test 4 - Verify response has all required fields
    def test_response_has_required_fields(self):
        response = requests.get(
            f"{BASE_URL}/weather",
            params={
                "q": VALID_CITY,
                "appid": API_KEY,
                "units": UNITS
            }
        )
        assert response.status_code == 200
        data = response.json()

        # Check all required fields exist
        required_fields = ["name", "main", "weather", "wind", "sys"]
        for field in required_fields:
            assert field in data, f"Missing field: {field}"

    # Test 5 - Verify humidity is between 0 and 100
    def test_humidity_is_valid(self):
        response = requests.get(
            f"{BASE_URL}/weather",
            params={
                "q": VALID_CITY,
                "appid": API_KEY,
                "units": UNITS
            }
        )
        assert response.status_code == 200
        data = response.json()
        humidity = data["main"]["humidity"]
        assert 0 <= humidity <= 100, f"Invalid humidity: {humidity}"