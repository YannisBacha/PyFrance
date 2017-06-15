class Dijkstra:
    def __init__(self, cities):
        self.cities = cities

    def compute_path(self, src_id, dst_id):
        tmp_cities = dict(self.cities)
        costs = {}
        fathers = {}
        for city_id in tmp_cities:
            costs[city_id] = float('inf')
            fathers[city_id] = None
        costs[src_id] = 0
        while len(tmp_cities) > 0:
            city_id = min(tmp_cities, key=lambda c_id: costs[c_id])
            if city_id == dst_id:
                break
            c = self.cities[city_id]
            del tmp_cities[city_id]
            for city, dist in c.neighbours:
                if city.id in tmp_cities:
                    if costs[city.id] > costs[city_id] + dist:
                        costs[city.id] = costs[city_id] + dist
                        fathers[city.id] = city_id
        if costs[dst_id] == float('inf'):
            return None
        path = [dst_id]
        while fathers[path[0]] is not None and fathers[path[0]] is not src_id:
            path.insert(0, fathers[path[0]])
        return path
