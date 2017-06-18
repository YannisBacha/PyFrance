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
    cost = 0
    i = 0
    for city_id in path:
        if i != 0:
            cost += Builder.haversine(cities[path[i]], cities[path[i - 1]])
        i += 1
        city = cities[city_id]
        json.append({'lat': city.coordinates.latitude,
                     'lng': city.coordinates.longitude,
                     'id': city.id,
                     'name': city.name})
    return json, cost


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
    path, cost = js_path(app.cities, Dijkstra(app.cities).compute_path(c1, c2))
    return jsonify({'status': 'ok',
                    'path': path,
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
    path, cost = js_path(app.cities, AStar(app.cities).compute_path(c1, c2))
    return jsonify({'status': 'ok',
                    'path': path,
                    'len': cost,
                    'algo': 'A*'})
