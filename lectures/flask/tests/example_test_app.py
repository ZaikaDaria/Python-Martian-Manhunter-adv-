import pytest
import json

from tests.conftest import client
from config import Config


def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200


def test_search_weather(client):
    Config.WEATHER_API_KEY = "776c974755msh3412d10ca84cccep13334ajsn4c81086b6ea1"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.post("/search", data={"city": "london"})
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for London" in response.data


def test_search_weather_mock(client, mocker):
    mocker.patch('requests.request', side_effect=ApiMock)
    response = client.post("/search", data={"cities": "Lviv"})
    assert response.status_code == 200
    print(response.data)
    assert b"Weather for Lviv" in response.data


class ApiMock:
    def __init__(self, *args, **kwargs):
        self.jsondata = {'message': 'accurate', 'cod': '200', 'count': 1, 'list': [
            {'id': 702550, 'name': 'Lviv', 'coord': {"lon": 24.0232, "lat": 49.8383},
             'main': {'temp': 21.32, 'feels_like': 21.13, 'temp_min': 20.78, 'temp_max': 22.81, 'pressure': 1015,
                      'humidity': 62}, 'dt': 1623487324, 'wind': {'speed': 3, 'deg': 280}, 'sys': {'country': 'UA'},
             'rain': None, 'snow': None, 'clouds': {'all': 40},
             'weather': [{"id": 802, "main": "Clouds", "description": "scattered clouds", "icon": "03d"}]}]}
        self.status_code = 200

    def json(self):
        return self.jsondata