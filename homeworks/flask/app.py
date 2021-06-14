from flask import Flask, render_template, request, Response
import requests
from config import Config
from flask_restful import Resource, Api

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


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

api = Api(app)

todos = {}


class Todo(Resource):

    def get(self, todo_id):
        try:
            data = {todo_id: todos[todo_id]}
        except KeyError:
            return Response("Not found", status=404)
        return data

    def put(self, todo_id):
        todos[todo_id] = request.json.get('text')
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        del todos[todo_id]
        return Response(todos, status=204)


class TodoList(Resource):

    def get(self):
        return todos

    def post(self):
        todos[request.json.get('todo_id', None)] = request.json.get('text', "")
        return todos


class Weather(Resource):

    def get(self):
        url = Config.WEATHER_API_URL

        cities = request.args.get('city')
        querystring = {"q": cities}

        headers = {
            'x-rapidapi-key': Config.WEATHER_API_KEY,
            'x-rapidapi-host': Config.WEATHER_API_HOST
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.text
            return  data

        return Response(status=404)


api.add_resource(Todo, '/todos/<int:todo_id>')
api.add_resource(TodoList, '/todos')
api.add_resource(Weather, '/weather')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')