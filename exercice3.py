from collections import deque

class Graphe:
    def __init__(self, sommets, oriente=False):
        self.sommets = sorted(sommets)
        self.oriente = oriente
        self.liste_adj = {sommet: [] for sommet in self.sommets}

    def ajouter_liaison(self, u, v):
        if u in self.liste_adj and v in self.liste_adj:
            self.liste_adj[u].append(v)
            if not self.oriente:
                self.liste_adj[v].append(u)

    def _bfs_distances_source(self, s):
        """Calcule les distances depuis un sommet source unique s"""
        visite = {sommet: False for sommet in self.sommets}
        dist_source = {sommet: -1 for sommet in self.sommets}  # -1 = inaccessible
        
        F = deque()
        
        # Initialisation avec la source s
        visite[s] = True
        dist_source[s] = 0
        F.append(s)  # Enfiler
        
        while F:
            u = F.popleft()  # Défiler
            
            for voisin in self.liste_adj[u]:
                if not visite[voisin]:
                    visite[voisin] = True
                    dist_source[voisin] = dist_source[u] + 1
                    F.append(voisin)  # Enfiler
                    
        return dist_source

    def calculer_matrice_distances(self):
        """Construit la matrice de distances pour tous les sommets"""
        matrice = {}
        for s in self.sommets:
            matrice[s] = self._bfs_distances_source(s)
        return matrice

    def afficher_matrice(self, matrice):
        """Affiche la matrice proprement sous forme de tableau"""
        # Affichage de l'en-tête (les sommets colonnes)
        print("   ", " ".join(f"{sommet:>3}" for sommet in self.sommets))
        print("   " + "-" * (4 * len(self.sommets)))
        
        # Affichage de chaque ligne
        for s in self.sommets:
            lignes_valeurs = []
            for x in self.sommets:
                val = matrice[s][x]
                # Pour l'affichage, on remplace -1 par '∞' (infini)
                lignes_valeurs.append(f"{val:>3}" if val != -1 else f"{'∞':>3}")
            print(f"{s} |", " ".join(lignes_valeurs))

# --- Zone de Test ---
if __name__ == "__main__":
    # Création du graphe de l'exercice (A à G)
    mes_sommets = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    g = Graphe(mes_sommets, oriente=False)
    
    # Ajout des liaisons du réseau
    g.ajouter_liaison('A', 'B')
    g.ajouter_liaison('A', 'C')
    g.ajouter_liaison('B', 'D')
    g.ajouter_liaison('B', 'E')
    g.ajouter_liaison('C', 'F')
    g.ajouter_liaison('C', 'G')
    
    # Calcul et affichage
    print("Calcul de la matrice des distances par parcours en largeur :")
    ma_matrice = g.calculer_matrice_distances()
    g.afficher_matrice(ma_matrice)