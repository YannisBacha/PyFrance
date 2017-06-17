import heapq

from pyfrance.computing.builder import Builder


class AStar:
    """
    Calcule le plus court chemin entre deux villes.
    Deux implémentations sont proposées:
        Avec un dictionnaire, le minimum est cherché de façon linéaire.
        Avec une priority queue, implémentée par heapq, le minimum est toujours en première position.
    """
    def __init__(self, cities):
        """
        Initialise l'algorithme.
        Les villes doivent être dans un dictionnaire, avec comme clé leur id et être de type City.

        :param cities: le dictionnaire des villes
        """
        self.cities = cities

    @staticmethod
    def heuristic(c1, c2):
        """
        Calcule l'heuristique de l'algorithme.
        La méthode choisie est la distance.

        :param c1: la première ville
        :param c2: la deuxième ville
        :return: l'heuristique
        """
        return Builder.haversine(c1, c2)

    def compute_path(self, src_id, dst_id):
        """
        Applique l'algorithme de Dijkstra.
        Le minimum est recherché linéairement selon le coût.

        :param src_id: l'id de la source
        :param dst_id: l'id de la destination
        :return: le chemin, une liste d'ids de villes
                 la longueur du chemin
        """
        tmp_cities = dict(self.cities)
        costs = {}
        fathers = {}
        for city_id in tmp_cities:
            costs[city_id] = float('inf')
            fathers[city_id] = None
        costs[src_id] = AStar.heuristic(self.cities[src_id], self.cities[dst_id])
        while len(tmp_cities) > 0:
            city_id = min(tmp_cities, key=lambda c_id: costs[c_id])
            if city_id == dst_id:
                break
            c = self.cities[city_id]
            del tmp_cities[city_id]
            for city, dist in c.neighbours:
                if city.id in tmp_cities:
                    h = AStar.heuristic(self.cities[city.id], self.cities[dst_id])
                    if costs[city.id] > costs[city_id] + dist + h:
                        costs[city.id] = costs[city_id] + dist + h
                        fathers[city.id] = city_id
        if costs[dst_id] == float('inf'):
            return None, None
        path = [dst_id]
        while fathers[path[0]] is not None and fathers[path[0]] is not src_id:
            path.insert(0, fathers[path[0]])
        return path, costs[dst_id]

    def compute_path_priority_queue(self, src_id, dst_id):
        """
        Applique l'algorithme de Dijkstra.
        Les coûts sont stockés dans un heapq. Le minimum est toujours placé devant.
        L'insertion et la suppression sont en O(log(n))

        :param src_id: l'id de la source
        :param dst_id: l'id de la destination
        :return: le chemin, une liste d'ids de villes
                 la longueur du chemin
        """
        tmp_cities = dict(self.cities)
        costs = {}
        costs_heap = []
        fathers = {}
        for city_id in tmp_cities:
            costs[city_id] = float('inf')
            fathers[city_id] = None
        costs[src_id] = AStar.heuristic(self.cities[src_id], self.cities[dst_id])
        heapq.heappush(costs_heap, (costs[src_id], src_id))
        while len(tmp_cities) > 0 and len(costs_heap) > 0:
            cost, city_id = heapq.heappop(costs_heap)
            if city_id == dst_id:
                break
            c = self.cities[city_id]
            if city_id not in tmp_cities:
                continue
            del tmp_cities[city_id]
            for city, dist in c.neighbours:
                if city.id in tmp_cities:
                    h = AStar.heuristic(self.cities[city.id], self.cities[dst_id])
                    if costs[city.id] > cost + dist + h:
                        costs[city.id] = cost + dist + h
                        heapq.heappush(costs_heap, (cost + dist + h, city.id))
                        fathers[city.id] = city_id
        if costs[dst_id] == float('inf'):
            return None, None
        path = [dst_id]
        while fathers[path[0]] is not None and fathers[path[0]] is not src_id:
            path.insert(0, fathers[path[0]])
        path.insert(0, src_id)
        return path, costs[dst_id]
