# PyFrance #
Voici notre projet de résolution de plus court chemin sur des communes
françaises.

PyFrance dispose de deux modes d'utilisation. Le mode console permet
de tester rapidement les fonctionnalités du logiciel. Le mode web
permet d'utiliser une interface claire et partique.

## Equipe ##
* [Yannis Bacha](https://github.com/YannisBacha)
* [Pierre Chat](https://github.com/TheCaptainCat)
* [Omran Haidari]()

## Algorithmes ##
Deux algorithmes sont implémentés dans PyFrance : Dijkstra et A*.
Chacun possède deux versions, avec une file de priorité ou sans.

Il est possible d'utiliser les deux versions des deux algorithmes.

## Mode console ##
Le mode console permet d'utiliser PyFrance sans installation de
bibliothèques tierces. Il suffit de lancer le fichier `main.py` avec
un interpréteur Python.

`$ python3 main.py` ou `$ python3.6 main.py`

L'utilisation de Python 3.5 ou 3.6 est requise, la version 2.7 ne
fonctionnera pas.

La suite de l'utilisation se fait en suivant les instructions sur la
console. Le choix des villes se fait grâce aux identifiants fournis
dans le fichier `resources/CommunesFrance.txt`

## Mode web ##

Le mode web offre une interface claire afin d'utiliser PyFrance.

Pour l'utiliser, il faut installer la bibliothèque Flask.

`$ pip install flask`

Assurez-vous d'installer Flask avec le bon `pip`. En cas de doute :
`$ pithon3 -m pip install flask` ou `$ pithon3.6 -m pip install flask`

Pour lancer le serveur :

`$ python3 run.py` ou `$ python3.6 run.py`

Il faut ensuite se rendre à l'adresse [localhost:5000](http://localhost:5000/).
La suite est expliquée sur l'application.