<<<<<<< HEAD
from flask import Flask, render_template, request, Response
import requests
from config import Config

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")
=======
# flask_web/app.py
from flask import Flask, render_template, request, jsonify, Response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
>>>>>>> 901413b908fc96f6859d83b2cfd3cb07aca60f7f

db = SQLAlchemy()

<<<<<<< HEAD
@app.route('/search', methods=['POST'])
def search_weather():
    weather = []
    cities = request.form.get("cities")
    cities = cities.replace(" ", "")
    c_list = cities.split(",")
    for city in c_list:
        querystring = {"q": city, "cnt": "1", "mode": "null", "lon": "0", "type": "link, accurate", "lat": "0",
                       "units": "metric"}
        headers = {
            'x-rapidapi-key': Config.WEATHER_API_KEY,
            'x-rapidapi-host': Config.WEATHER_API_HOST
        }
        response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            try:
                weather.append(data['list'][0])
            except(IndexError, ):
                return Response(status=404)
        else:
            return Response(status=404)
    return render_template("weather.html", weather=weather)


@app.route('/search_lat_lon', methods=['POST'])
def search_weather_lat_lan():
    weather = []
    lat = request.form.get("lat")
    lon = request.form.get("lon")
    querystring = {"q": "", "cnt": "1", "mode": "null", "lon": lon, "type": "link, accurate", "lat": lat,
                   "units": "metric"}
    headers = {
        'x-rapidapi-key': Config.WEATHER_API_KEY,
        'x-rapidapi-host': Config.WEATHER_API_HOST
    }
    response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
    data = response.json()
    if response.status_code == 200:
        weather.append(data['list'][0])
        return render_template("weather.html", weather=weather)
    else:
        return Response(status=404)
=======
app = Flask(__name__)

app.config.from_object("config.Config")

api = Api(app)

db.init_app(app)

with app.app_context():
    import routes.todo
    import routes.weather
    import routes.blog
    from models.models import User, Article, Category

    db.create_all()

>>>>>>> 901413b908fc96f6859d83b2cfd3cb07aca60f7f


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')