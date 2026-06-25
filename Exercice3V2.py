from collections import deque

def charger_graphe(nom_fichier):
    """Lit un fichier texte pour générer la liste d'adjacence et les sommets"""
    liste_adj = {}
    sommets_set = set()
    
    with open(nom_fichier, 'r', encoding='utf-8') as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:  # Ignore les lignes vides
                continue
            
            # On découpe la ligne en deux sommets
            u, v = ligne.split()
            
            sommets_set.add(u)
            sommets_set.add(v)
            
            # Initialisation des listes si nécessaire
            if u not in liste_adj: liste_adj[u] = []
            if v not in liste_adj: liste_adj[v] = []
            
            # Ajout des liaisons (Graphe non-orienté)
            liste_adj[u].append(v)
            liste_adj[v].append(u)
            
    # On trie les sommets pour avoir un affichage propre (A, B, C...)
    return liste_adj, sorted(list(sommets_set))

def bfs_distances_source(liste_adj, sommets, s):
    """Calcule les distances depuis un sommet source unique s (Même logique que le cours)"""
    visite = {sommet: False for sommet in sommets}
    dist_source = {sommet: -1 for sommet in sommets}
    
    F = deque()
    
    visite[s] = True
    dist_source[s] = 0
    F.append(s)
    
    while F:
        u = F.popleft()
        
        # Si un sommet n'a pas de voisins dans la liste d'adjacence (sommet isolé)
        if u not in liste_adj:
            continue
            
        for voisin in liste_adj[u]:
            if not visite[voisin]:
                visite[voisin] = True
                dist_source[voisin] = dist_source[u] + 1
                F.append(voisin)
                
    return dist_source

def calculer_matrice_distances(liste_adj, sommets):
    """Génère la matrice globale en bouclant sur tous les sommets"""
    matrice = {}
    for s in sommets:
        matrice[s] = bfs_distances_source(liste_adj, sommets, s)
    return matrice

def sauvegarder_matrice(nom_fichier, sommets, matrice):
    """Enregistre la matrice finale dans un fichier texte formaté"""
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        # 1. Écriture de l'en-tête (les colonnes)
        en_tete = "    " + " ".join(f"{sommet:>3}" for sommet in sommets) + "\n"
        f.write(en_tete)
        f.write("    " + "-" * (4 * len(sommets)) + "\n")
        
        # 2. Écriture des lignes
        for s in sommets:
            lignes_valeurs = []
            for x in sommets:
                val = matrice[s][x]
                lignes_valeurs.append(f"{val:>3}" if val != -1 else f"{'∞':>3}")
            
            ligne_complete = f"{s} | " + " ".join(lignes_valeurs) + "\n"
            f.write(ligne_complete)

# --- Programme Principal ---
if __name__ == "__main__":
    fichier_entree = "graphe_entre.txt"
    fichier_sortie = "matrice_sorties.txt"
    
    print(f"1. Lecture du fichier {fichier_entree}...")
    reseau_adj, les_sommets = charger_graphe(fichier_entree)
    
    print("2. Calcul des distances (BFS)...")
    matrice_finale = calculer_matrice_distances(reseau_adj, les_sommets)
    
    print(f"3. Enregistrement des résultats dans {fichier_sortie}...")
    sauvegarder_matrice(fichier_sortie, les_sommets, matrice_finale)
    
    print("Terminé ! Ouvrez le fichier 'matrice_sorties.txt' pour voir le résultat.")