import codecs
import csv

from pyfrance.city import City


class Parser:
    """Parse a csv file containing cities with coordinates"""
    def __init__(self, filename, max_pop=None):
        self.filename = filename
        self.cities = set()
        self.max_pop = max_pop

    def parse(self):
        with codecs.open(self.filename, 'r', encoding='utf-8', errors='ignore') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[1] == 'nom':
                    continue
                c = City(row[0], row[1], int(row[2]), float(row[4].replace(',', '.')), float(row[3].replace(',', '.')))
                if self.max_pop is None or self.max_pop < c.population:
                    self.cities.add(c)
