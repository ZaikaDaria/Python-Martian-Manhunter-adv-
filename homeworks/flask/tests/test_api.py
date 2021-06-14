from tests.conftest import client, todos
import json
from config import Config


def test_create(client, todos):
    headers = {
        "Content-Type": "application/json"
    }
    response = client.post("/todos", headers=headers, json=todos)
    assert response.status_code == 200
    assert response.json['1'] == "text"


def test_list(client):
    response = client.get('/todos')
    assert response.status_code == 200
    assert response.json['1'] == "text"


def test_update(client):
    update_data = {
        "text": "blablabla"
    }

    response = client.put("/todos/1", json=update_data)
    assert response.status_code == 200
    get_response = client.get("/todos/1")
    assert get_response.status_code == 200
    assert get_response.json['1'] == "blablabla"


def test_delete(client):
    response = client.delete("/todos/1")
    assert response.status_code == 204
    response = client.get("/todos/1")
    assert response.status_code == 404

def test_weather(client):
    Config.WEATHER_API_KEY = "eb693de49dmsh5020a2f638740f4p1f0889jsnf4b5bc7fbd2f"
    Config.WEATHER_API_URL="https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST="community-open-weather-map.p.rapidapi.com"
    response = client.get('/weather?city=Lviv')
    assert response.status_code == 404
    response = client.get('/weather?city=London,Lviv,Kiev')
    assert response.status_code == 404
    response = client.get('/weather?city=, ,')
    assert response.status_code == 404
    response = client.get('/weather?city=London, L')
    assert response.status_code == 404
    response = client.get('/weather?city=L')
    assert response.status_code == 404