import heapq


class Dijkstra:
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

    def compute_path(self, src_id, dst_id):
        """
        Applique l'algorithme de Dijkstra.
        Le minimum est recherché linéairement selon le coût.

        :param src_id: l'id de la source
        :param dst_id: l'id de la destination
        :return: le chemin, une liste d'ids de villes
        """
        fathers = {src_id: None}
        cities_ids = set()
        costs = {}
        for city_id in self.cities:
            costs[city_id] = float('inf')
            cities_ids.add(city_id)
        costs[src_id] = 0
        while len(cities_ids) > 0:
            current_id = min(cities_ids, key=lambda x: costs[x])
            if current_id == dst_id:
                break
            cities_ids.remove(current_id)
            for neighbour, dist in self.cities[current_id].neighbours:
                if neighbour.id not in cities_ids:
                    continue
                tmp_score = costs[current_id] + dist
                if tmp_score < costs[neighbour.id]:
                    fathers[neighbour.id] = current_id
                    costs[neighbour.id] = tmp_score
        if costs[dst_id] == float('inf'):
            return None
        path = [dst_id]
        while fathers[path[0]] is not None:
            path.insert(0, fathers[path[0]])
        return path

    def compute_path_priority_queue(self, src_id, dst_id):
        """
        Applique l'algorithme de Dijkstra.
        Les coûts sont stockés dans un heapq. Le minimum est toujours placé devant.
        L'insertion et la suppression sont en O(log(n))

        :param src_id: l'id de la source
        :param dst_id: l'id de la destination
        :return: le chemin, une liste d'ids de villes
        """
        fathers = {src_id: None}
        cities_ids = set()
        costs = {}
        costs_heap = []
        for city_id in self.cities:
            costs[city_id] = float('inf')
            cities_ids.add(city_id)
        costs[src_id] = 0
        heapq.heappush(costs_heap, (0, src_id))
        while len(cities_ids) > 0:
            current_id = heapq.heappop(costs_heap)[1]
            """if current_id not in cities_ids:
                continue"""
            if current_id == dst_id:
                break
            cities_ids.remove(current_id)
            for neighbour, dist in self.cities[current_id].neighbours:
                if neighbour.id not in cities_ids:
                    continue
                tmp_score = costs[current_id] + dist
                if tmp_score < costs[neighbour.id]:
                    fathers[neighbour.id] = current_id
                    costs[neighbour.id] = tmp_score
                    costs_heap = [x for x in costs_heap if x[1] != neighbour.id]
                    heapq.heappush(costs_heap, (costs[neighbour.id] + dist, neighbour.id))
        if costs[dst_id] == float('inf'):
            return None
        path = [dst_id]
        while fathers[path[0]] is not None:
            path.insert(0, fathers[path[0]])
        return path
