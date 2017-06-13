import codecs
import csv

from pyfrance.city import City


class Parser:
    """Parse a csv file containing cities with coordinates"""
    def __init__(self, filename):
        self.filename = filename
        self.cities = set()

    def parse(self):
        with codecs.open(self.filename, 'r', encoding='utf-8', errors='ignore') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[1] == 'nom':
                    continue
                c = City(row[0], row[1], row[2], row[3], row[4])
                self.cities.add(c)
