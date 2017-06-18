from time import time

from pyfrance.computing import Builder, Parser
from pyfrance.pathfinding import Dijkstra, AStar


class Console:
    """Permet la gestion de l'application sur la console."""
    @staticmethod
    def run():

        def algorithm(fn, c1, c2):
            return fn(c1, c2)

        pop = None
        while pop is None:
            try:
                pop = int(input('Choisissez la population minimale d\'une ville : '))
            except ValueError:
                print('Erreur de saisie')
                continue
        dist = None
        while dist is None:
            try:
                dist = int(input('Choisissez la distance maximale entre deux villes : '))
            except ValueError:
                print('Erreur de saisie')
                continue
        print('Création des villes...')
        p = Parser('resources/CommunesFrance.csv', pop)
        t1 = time()
        n = p.parse()
        print('{0} villes créées en {1}s'.format(n, time() - t1))
        print('Construction du graphe...')
        b = Builder(p.cities, dist)
        t1 = time()
        l = b.build()
        print('{0} connexions créées en {1}s'.format(l, time() - t1))
        while True:
            print("Choisissez un algorithme\n1) Dijkstra\n"
                  + "2) Dijkstra avec file de priorité\n3) A*\n4) A* avec file de priorité\n5) Stop")
            c = None
            while c is None or not 1 <= c <= 5:
                try:
                    c = int(input('Faites votre choix : '))
                except ValueError:
                    print('Erreur de saisie')
                    continue
            if c == 5:
                print('Au revoir !')
                exit()
            c1 = None
            while c1 is None or c1 not in p.cities:
                if c1 is not None:
                    print('Cet identifiant n\'existe pas')
                c1 = input('Choisissez la première ville : ')
            c2 = None
            while c2 is None or c2 not in p.cities:
                if c2 is not None:
                    print('Cet identifiant n\'existe pas')
                c2 = input('Choisissez la deuxième ville : ')
            path = None
            t1 = time()
            if c == 1:
                path = algorithm(Dijkstra(p.cities).compute_path, c1, c2)
            elif c == 2:
                path = algorithm(Dijkstra(p.cities).compute_path_priority_queue, c1, c2)
            elif c == 3:
                path = algorithm(Dijkstra(p.cities).compute_path, c1, c2)
            elif c == 4:
                path = algorithm(Dijkstra(p.cities).compute_path_priority_queue, c1, c2)
            print('Chemin calculé en {0}s'.format(time() - t1))
            print(path)
