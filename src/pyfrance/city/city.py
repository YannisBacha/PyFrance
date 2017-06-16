from .coordinates import Coordinates


class City:
    """Représente une ville."""

    def __init__(self, id, name, population, latitude, longitude):
        """
        Crée une ville.

        :param id: l'id de la ville
        :param name: le nom de la ville
        :param population: le nombre d'habitants dans la ville
        :param latitude: la latitude de la ville
        :param longitude: la longitude de la ville
        """
        self.id = id
        self.name = name
        self.population = population
        self.coordinates = Coordinates(latitude, longitude)
        self.neighbours = set()

    def add_neighbour(self, city, dist):
        """
        Ajoute un voisin à la ville.
        Les voisins sont stockés dans un tuple:
            (ville, distance)

        :param city: la ville
        :param dist: la distance
        """
        self.neighbours.add((city, dist))

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.id, self.name, self.population, self.coordinates)

    def __repr__(self):
        return str(self)
