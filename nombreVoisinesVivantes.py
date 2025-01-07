def nombreVoisinesVivantes(g, i, j):
    # Appeler la fonction positionsCasesVoisines pour obtenir les voisins de la cellule (i, j)
    voisins = positionsCasesVoisines(g, i, j)
    
    # Initialiser un compteur pour les voisins vivants
    nombre_vivants = 0
    
    # Parcourir les voisins et compter ceux qui sont vivants
    for ni, nj in voisins:
        if g[ni][nj]:  # Vérifie si la case est vivante
            nombre_vivants += 1
    
    return nombre_vivants
