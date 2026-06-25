📌 Présentation du Projet

Le projet consiste en une application Python capable de modéliser, manipuler, analyser et visualiser des graphes (orientés et non orientés) à l'aide de structures de données standardisées (listes d'adjacence, matrices d'adjacence).

Le programme permet à l'utilisateur de charger des graphes depuis des fichiers texte simples, d'analyser automatiquement toutes leurs propriétés fondamentales, de calculer des matrices de distances, d'exécuter des algorithmes d'optimisation classiques (comme la recherche d'arbres couvrants minimums), et de sauvegarder les résultats détaillés dans des fichiers de sortie formatés.

🚀 Fonctionnalités Clés

1. Modélisation et Caractérisation (TP1 - Noyau Algorithmique)

Calcul des métriques fondamentales :

Ordre du graphe : Nombre total de sommets ($N$).

Taille du graphe : Nombre total de liaisons ($M$ - arcs ou arêtes).

Degré des sommets : Calcul du degré simple pour les graphes non orientés, et distinction entre degré entrant et degré sortant pour les graphes orientés.

Représentations structurales :

Génération de la liste d'adjacence dynamique (optimisée pour l'espace mémoire).

Génération de la matrice d'adjacence carrée (représentation algébrique $N \times N$).

Extraction de la liste complète des arcs (orientés) ou arêtes (non orientés).

2. Gestion de Fichiers Robustes & Auto-détection

Parsing intelligent d'entrées : Lecture de fichiers textes délimitant les liaisons avec gestion automatique de la nature du graphe (orienté / non orienté) via une en-tête personnalisée (Type: oriente ou Type: non_oriente).

Traitement de chaînes : Nettoyage rigoureux des données avec gestion robuste des espaces et retours à la ligne (strip() et split()).

Export formaté : Écriture automatique des résultats et rapports d'analyse au format .txt.

3. Interface Graphique Interactive (GUI - Tkinter)

Pour faciliter l'interaction, une interface utilisateur "clé en main" a été développée en Tkinter :

Saisie double-canal : L'utilisateur peut importer un fichier .txt existant ou écrire/modifier directement les liaisons dans un éditeur de texte intégré.

Visualisation immédiate : Affichage en temps réel des résultats de l'analyse structurelle du graphe à l'écran.

Téléchargement assisté : Intégration d'une boîte de dialogue système (filedialog) pour sauvegarder les sorties analytiques n'importe où sur l'ordinateur de l'utilisateur.

🛠️ Concepts & Algorithmes Avancés Intégrés

Au fil des travaux pratiques, le noyau algorithmique a été enrichi pour intégrer :

Parcours en Largeur (BFS) & Distances : Calcul de la matrice globale des distances géodésiques entre chaque paire de sommets à l'aide d'une structure de File FIFO (collections.deque).

Parcours en Profondeur (DFS) & Détection de Cycles : Implémentation de la coloration à trois états (NON, EN_COURS, TERMINE) pour détecter d'éventuels cycles (boucles fermées).

Algorithme de Dijkstra : Détermination des plus courts chemins valués et reconstruction dynamique des chemins optimaux (chaînes de prédécesseurs).

Arbres Couvrants de Poids Minimum (MST) : Implémentations comparatives de l'algorithme de Prim-Jarník (approche par frontière gloutonne) et de Kruskal (approche par union de forêts disjointes via la structure de données Union-Find).

📁 Format des Fichiers

Fichier d'entrée standardisé (entree_graphe.txt)

Le fichier d'entrée se structure ainsi : la première ligne définit le type, les suivantes définissent les arcs/arêtes par ligne (avec ou sans poids) :

Type: non_oriente
x1 x8 2
x1 x2 4
x8 x2 1
x2 x6 3


Fichier de sortie généré (resultat_graphe.txt)

Le programme génère un rapport lisible contenant les structures de données formatées :

=== CARACTERISTIQUES DU GRAPHE ===

Type : Non orienté (Arêtes)
Ordre du graphe : 4
Taille du graphe : 4

Liste d'adjacence :
  x1 : ['x2', 'x8']
  x2 : ['x1', 'x6', 'x8']
  x6 : ['x2']
  x8 : ['x1', 'x2']

Matrice d'adjacence :
  [0, 1, 0, 1]
  [1, 0, 1, 1]
  [0, 1, 0, 0]
  [1, 1, 0, 0]


⚙️ Installation et Exécution

Prérequis

Python 3.8 ou supérieur installé sur votre système.

La bibliothèque d'interface graphique Tkinter est nativement incluse avec l'installation standard de Python (aucune commande pip requise).

Exécuter l'application principale (GUI)

Clonez ce dépôt sur votre machine locale :

git clone [https://github.com/votre-nom-utilisateur/nom-du-repo.git](https://github.com/votre-nom-utilisateur/nom-du-repo.git)
cd nom-du-repo


Lancez le script de l'interface graphique :

python app_graphe.py


Suivez les instructions affichées à l'écran pour charger votre graphe et exporter les résultats !

🏗️ Architecture du Code (MVC de base)

Le code est structuré selon de bonnes pratiques de développement orienté objet :

Modèle (Graphe) : Gère la structure interne mathématique du graphe, l'importation de fichiers, le calcul des matrices et l'exécution des algorithmes.

Vue (ApplicationGraphe) : Gère l'affichage de l'interface utilisateur, la capture des événements, les boîtes de dialogue de sauvegarde et les contrôleurs de saisie de texte.

Développé dans le cadre du projet académique d'Intelligence Artificielle & Big Data