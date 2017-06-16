from flask import render_template, jsonify
from flask import Flask

from pyfrance.computing import Parser, Builder
from pyfrance.pathfinding import Dijkstra


def parse_cities():
    p = Parser('resources/CommunesFrance.csv', 10000)
    p.parse()
    return p.cities


def create_cities_list(cities):
    c_list = []
    for city in cities.values():
        c_list.append({'id': city.id,
                       'name': city.name,
                       'lat': city.coordinates.latitude,
                       'lng': city.coordinates.longitude})
    c_list.sort(key=lambda x: x['id'])
    return c_list


def js_path(cities, path):
    json = []
    for city_id in path:
        city = cities[city_id]
        json.append({'lat': city.coordinates.latitude,
                     'lng': city.coordinates.longitude,
                     'id': city.id,
                     'name': city.name})
    return json


def build_graph(cities):
    b = Builder(cities, 50)
    b.build()


app = Flask(__name__)
app.debug = True
app.cities = parse_cities()
app.cities_list = create_cities_list(app.cities)
build_graph(app.cities)


@app.route('/')
def hello_world():
    return render_template('test.html', cities=app.cities_list)


@app.route('/cities')
def get_cities():
    return jsonify(app.cities)


@app.route('/path/dijkstra/<string:c1>/<string:c2>')
def dijkstra(c1, c2):
    dijkstra = Dijkstra(app.cities)
    path = dijkstra.compute_path(c1, c2)
    return jsonify(js_path(app.cities, path))
