import requests
from config import API_KEY, BASE_URL, VALID_CITY, UNITS

class TestWeatherForecast:

    # Test 1 - Get 5 day forecast
    def test_get_5day_forecast(self):
        response = requests.get(
            f"{BASE_URL}/forecast",
            params={
                "q": VALID_CITY,
                "appid": API_KEY,
                "units": UNITS
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "list" in data
        assert len(data["list"]) > 0

    # Test 2 - Forecast returns 40 items (5 days x 8 per day)
    def test_forecast_returns_40_items(self):
        response = requests.get(
            f"{BASE_URL}/forecast",
            params={
                "q": VALID_CITY,
                "appid": API_KEY,
                "units": UNITS
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert len(data["list"]) == 40

    # Test 3 - Each forecast item has required fields
    def test_forecast_items_have_required_fields(self):
        response = requests.get(
            f"{BASE_URL}/forecast",
            params={
                "q": VALID_CITY,
                "appid": API_KEY,
                "units": UNITS
            }
        )
        assert response.status_code == 200
        data = response.json()

        for item in data["list"]:
            assert "dt" in item          # timestamp
            assert "main" in item