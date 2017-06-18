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
        Applique l'algorithme de A*.
        Le minimum est recherché linéairement selon le coût.

        :param src_id: l'id de la source
        :param dst_id: l'id de la destination
        :return: le chemin, une liste d'ids de villes
        """
        dst = self.cities[dst_id]
        fathers = {src_id: None}
        open_c = set()
        open_c.add(src_id)
        closed_c = set()
        costs = {}
        h_costs = {}
        for city_id in self.cities:
            costs[city_id] = float('inf')
            h_costs[city_id] = float('inf')
        costs[src_id] = 0
        h_costs[src_id] = AStar.heuristic(self.cities[src_id], dst)
        while len(open_c) > 0:
            current_id = min(open_c, key=lambda x: h_costs[x])
            if current_id == dst_id:
                break
            open_c.remove(current_id)
            closed_c.add(current_id)
            for neighbour, dist in self.cities[current_id].neighbours:
                if neighbour.id in closed_c:
                    continue
                if neighbour.id not in open_c:
                    open_c.add(neighbour.id)
                t_g_score = costs[current_id] + dist
                if t_g_score >= costs[neighbour.id]:
                    continue
                fathers[neighbour.id] = current_id
                costs[neighbour.id] = t_g_score
                h_costs[neighbour.id] = costs[neighbour.id] + AStar.heuristic(neighbour, dst)
        if costs[dst_id] == float('inf'):
            return None
        path = [dst_id]
        while fathers[path[0]] is not None:
            path.insert(0, fathers[path[0]])
        return path

    def compute_path_priority_queue(self, src_id, dst_id):
        """
        Applique l'algorithme de A*.
        Les coûts sont stockés dans un heapq. Le minimum est toujours placé devant.
        L'insertion et la suppression sont en O(log(n))

        :param src_id: l'id de la source
        :param dst_id: l'id de la destination
        :return: le chemin, une liste d'ids de villes
        """
        dst = self.cities[dst_id]
        fathers = {src_id: None}
        open_c = set()
        open_c.add(src_id)
        closed_c = set()
        costs = {}
        h_costs = []
        for city_id in self.cities:
            costs[city_id] = float('inf')
        costs[src_id] = 0
        heapq.heappush(h_costs, (AStar.heuristic(self.cities[src_id], dst), src_id))
        while len(open_c) > 0:
            current_id = heapq.heappop(h_costs)[1]
            if current_id in closed_c:
                continue
            if current_id == dst_id:
                break
            open_c.remove(current_id)
            closed_c.add(current_id)
            for neighbour, dist in self.cities[current_id].neighbours:
                if neighbour.id in closed_c:
                    continue
                if neighbour.id not in open_c:
                    open_c.add(neighbour.id)
                t_g_score = costs[current_id] + dist
                if t_g_score >= costs[neighbour.id]:
                    continue
                fathers[neighbour.id] = current_id
                costs[neighbour.id] = t_g_score
                heapq.heappush(h_costs, (costs[neighbour.id] + AStar.heuristic(neighbour, dst), neighbour.id))
        if costs[dst_id] == float('inf'):
            return None
        path = [dst_id]
        while fathers[path[0]] is not None:
            path.insert(0, fathers[path[0]])
        return path
