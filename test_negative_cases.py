import requests
from config import API_KEY, BASE_URL, INVALID_CITY, UNITS

class TestNegativeCases:

    # Test 1 - Invalid city name
    def test_invalid_city_returns_404(self):
        response = requests.get(
            f"{BASE_URL}/weather",
            params={
                "q": INVALID_CITY,
                "appid": API_KEY,
                "units": UNITS
            }
        )
        assert response.status_code == 404
        data = response.json()
        assert data["cod"] == "404"
        assert "message" in data

    # Test 2 - Invalid API key
    def test_invalid_api_key_returns_401(self):
        response = requests.get(
            f"{BASE_URL}/weather",
            params={
                "q": "London",
                "appid": "invalid_key_123",
                "units": UNITS
            }
        )
        assert response.status_code == 401
        data = response.json()
        assert data["cod"] == 401

    # Test 3 - Missing city parameter
    def test_missing_city_returns_400(self):
        response = requests.get(
            f"{BASE_URL}/weather",
            params={
                "appid": API_KEY,
                "units": UNITS
            }
        )
        assert response.status_code == 400
        data = response.json()
        assert data["cod"] == "400"

    # Test 4 - Empty city name
    def test_empty_city_returns_400(self):
        response = requests.get(
            f"{BASE_URL}/weather",
            params={
                "q": "",
                "appid": API_KEY,
                "units": UNITS
            }
        )
        assert response.status_code == 400

    # Test 5 - Invalid units parameter
    def test_invalid_units_still_returns_200(self):
        response = requests.get(
            f"{BASE_URL}/weather",
            params={
                "q": "London",
                "appid": API_KEY,
                "units": "invalidunit"
            }
        )
        # API defaults to standard units if invalid unit given
        assert response.status_code == 200

    # Test 6 - City name with special characters
    def test_city_with_numbers_returns_404(self):
        response = requests.get(
            f"{BASE_URL}/weather",
            params={
                "q": "City12345",
                "appid": API_KEY,
                "units": UNITS
            }
        )
        assert response.status_code == 404

    # Test 7 - Verify error response has message field
    def test_error_response_has_message(self):
        response = requests.get(
            f"{BASE_URL}/weather",
            params={
                "q": INVALID_CITY,
                "appid": API_KEY,
                "units": UNITS
            }
        )
        assert response.status_code == 404
        data = response.json()
        assert "message" in data
        assert data["message"] != ""