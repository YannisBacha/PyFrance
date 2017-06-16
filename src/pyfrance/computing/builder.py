from math import radians, cos, sin, asin, sqrt


class Builder:
    """
    Construit le graphe.
    """

    def __init__(self, cities, max_dist=None):
        """
        Initialise l'algorithme.
        Les villes doivent être de type City et stockées dans un ensemble (set()).

        :param cities: l'ensemble des villes
        :param max_dist: la longueur maximale d'un lien entre deux villes
        """
        self.cities = cities
        self.max_dist = max_dist

    def build(self):
        """
        Construit le graphe.
        Pour chaque ville, la liste de ses voisins est remplie avec les villes à proximité.
        La longueur maximale d'un lien est un paramètre de la classe.

        :return: le nombre de liens créés
        """
        links = 0
        for key1 in self.cities:
            city = self.cities[key1]
            for key2 in self.cities:
                other = self.cities[key2]
                if city != other and other not in city.neighbours:
                    dist = Builder.haversine(city, other)
                    if self.max_dist is None or self.max_dist > dist:
                        city.add_neighbour(other, dist)
                        other.add_neighbour(city, dist)
                        links += 1
        return links

    @staticmethod
    def haversine(c1, c2):
        """
        Calcule la distance entre deux villes.

        :param c1: première ville
        :param c2: deuxième ville
        :return: la distance entre les deux villes
        """
        lon1, lat1, lon2, lat2 = map(radians,
                                     [c1.coordinates.longitude, c1.coordinates.latitude, c2.coordinates.longitude,
                                      c2.coordinates.latitude])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r
