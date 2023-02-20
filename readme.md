# Cartographie réseau Annecy

## Presentation : 
Projet de cartographie du réseau de transport en commum de la ville d'Annecy et de ses alentours via le logiciel Gephi (logiciel libre d'analyse et de visualisation de réseaux).

Le fichier mère 'get data\address.xlsx' permet de référencer tous le réseau. Chaque arrêt de bus et présent. 
* id
* label : nom de l'arrêt
* edges : reprèsentant les liens entre chaque arrêts
* coord : si label introuvable ou incorrect, saisie des coordonnées géographiques.

Le fichier 'get data\saveNodesData' permet de parcourir le fichier Excel pour créer un fichier nodes.csv contenant les noeuds (chaque arrêt de bus).

Le fichier 'get data\saveEdgesData' permet de parcourir le fichier Excel pour créer un fichier edges.csv contenant les liens.

## Installation packages et exécution scrip : 
```
pip install geopy 
pip install pandas
```
Exécuter le fichier python 'get data\saveNodesData' ou exécuter 'get data\GenerateDataset.bat' (le deuxième fichier python pour les liens sera automatiquement exécuté).

Quelques minutes sont nécéssaire pour récupérer l'ensemble des coordonnées géographiques.


## Visualisation Gephi : 

Installé le package Geo Layout.
Importer les fichiers nodes puis edges.

Générer la spécialisation via les coordonnées géographique (voir paramètres 'GeoLayout Settings.png').



Les arrêts sont correctement positionnés !

<img src="data graphs\result map\grand_annecy.jpg"  style="display: inline-block; margin: 0 auto; max-width: 600px">