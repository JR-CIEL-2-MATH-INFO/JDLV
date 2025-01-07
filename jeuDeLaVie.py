def jeuDeLaVie(g):
    # Créer une nouvelle grille pour stocker les états suivants
    nouvelles_grilles = [[False] * len(g[0]) for _ in range(len(g))]
    
    # Parcourir toutes les cellules de la grille
    for i in range(len(g)):
        for j in range(len(g[0])):
            # Calculer l'état suivant de chaque cellule
            nouvelles_grilles[i][j] = etatSuivant(g, i, j)
    
    # Remplacer la grille d'origine par la nouvelle grille mise à jour
    for i in range(len(g)):
        for j in range(len(g[0])):
            g[i][j] = nouvelles_grilles[i][j]
