def etatSuivant(g, i, j):
    # Récupérer les voisins de la cellule (i, j)
    voisins = positionsCasesVoisines(g, i, j)
    
    # Compter le nombre de voisins vivants
    voisins_vivants = nombreVoisinesVivantes(g, i, j)
    
    # Récupérer l'état actuel de la cellule (i, j)
    etat_actuel = g[i][j]
    
    # Appliquer les règles du Jeu de la Vie
    if etat_actuel:  # Si la cellule est vivante
        if voisins_vivants == 2 or voisins_vivants == 3:
            return True  # Reste vivante
        else:
            return False  # Meurt
    else:  # Si la cellule est morte
        if voisins_vivants == 3:
            return True  # Devient vivante
        else:
            return False  # Reste morte
