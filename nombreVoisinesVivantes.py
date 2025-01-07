def nombreVoisinesVivantes(g, i, j):
    # Appeler la fonction positionsCasesVoisines pour obtenir les voisins de la cellule (i, j)
    voisins = positionsCasesVoisines(g, i, j)
    
    # Initialiser un compteur pour les voisins vivants
    nombre_vivants = 0
    
    # Parcourir les voisins et compter ceux qui sont vivants
    for ni, nj in voisins:
        if g[ni][nj]:  # Vérifie si la case est vivante
            #nombre_vivants = ..........
    
    return nombre_vivants

grille = [
    [False, False, False, False, False],
    [False, True,  True,  True,  False],
    [False, False, True,  False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
]

# Test de la fonction
# À compléter : choisissez une cellule à tester, par exemple (1, 2)
# voisins = positionsCasesVoisines(grille, ..., ...)
# print("Voisins :", voisins)

