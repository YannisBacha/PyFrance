from flask import render_template, jsonify
from flask import Flask

from pyfrance.computing import Parser, Builder
from pyfrance.pathfinding import Dijkstra, AStar


def parse_cities(pop):
    p = Parser('resources/CommunesFrance.csv', pop)
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
    if path is None:
        return None
    json = []
    for city_id in path:
        city = cities[city_id]
        json.append({'lat': city.coordinates.latitude,
                     'lng': city.coordinates.longitude,
                     'id': city.id,
                     'name': city.name})
    return json


def build_graph(cities, dist):
    b = Builder(cities, dist)
    b.build()


app = Flask(__name__)
app.debug = True
app.cities = None
app.cities_list = None


@app.route('/')
def hello_world():
    return render_template('test.html')


@app.route('/parse/<int:pop>/<int:dist>')
def parse(pop, dist):
    app.cities = parse_cities(pop)
    app.cities_list = create_cities_list(app.cities)
    build_graph(app.cities, dist)
    return jsonify({'status': 'ok',
                    'list': app.cities_list})


@app.route('/cities')
def get_cities():
    if app.cities_list is None:
        return jsonify({'status': 'empty'})
    return jsonify({'status': 'ok', 'list': app.cities_list})


@app.route('/path/dijkstra/<string:c1>/<string:c2>')
def dijkstra(c1, c2):
    if app.cities is None:
        return jsonify({'status': 'error',
                        'message': 'Le graphe n\'est pas construit'})
    if c1 not in app.cities or c2 not in app.cities:
        return jsonify({'status': 'error',
                        'message': 'Un identifiant n\'existe pas'})
    dijkstra = Dijkstra(app.cities)
    path, cost = dijkstra.compute_path(c1, c2)
    return jsonify({'status': 'ok',
                    'path': js_path(app.cities, path),
                    'len': cost,
                    'algo': 'Dijkstra'})


@app.route('/path/astar/<string:c1>/<string:c2>')
def astar(c1, c2):
    if app.cities is None:
        return jsonify({'status': 'error',
                        'message': 'Le graphe n\'est pas construit'})
    if c1 not in app.cities or c2 not in app.cities:
        return jsonify({'status': 'error',
                        'message': 'Un identifiant n\'existe pas'})
    astar = AStar(app.cities)
    path, cost = astar.compute_path(c1, c2)
    return jsonify({'status': 'ok',
                    'path': js_path(app.cities, path),
                    'len': cost,
                    'algo': 'A*'})
