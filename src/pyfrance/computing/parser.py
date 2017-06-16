import codecs
import csv

from pyfrance.city import City


class Parser:
    """Lis le fichier contenant les villes et les crée."""
    def __init__(self, filename, min_pop=None):
        """
        Initialise un nouveau parser.

        :param filename: le nom du fichier, relativement à main.py
        :param min_pop: la population minimale à atteindre pour créer la ville
        """
        self.filename = filename
        self.cities = {}
        self.min_pop = min_pop

    def parse(self):
        """
        Lis le fichier et crée les villes.
        Elles sont stockées dans un ensemble (set).

        :return: le nombre de villes créées.
        """
        with codecs.open(self.filename, 'r', encoding='utf-8', errors='ignore') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[1] == 'nom':
                    continue
                c = City(row[0], row[1], int(row[2]), float(row[4].replace(',', '.')), float(row[3].replace(',', '.')))
                if self.min_pop is None or self.min_pop < c.population:
                    self.cities[c.id] = c
        return len(self.cities)
