def positionsCasesVoisines(g, i, j):
    voisins = []
    lignes = len(g)
    colonnes = len(g[0])

    # Liste des directions possibles : haut, bas, gauche, droite, diagonales
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for di, dj in directions:
        ni, nj = i + di, j + dj
        # Vérifier si la nouvelle position est dans les limites de la grille
        if 0 <= ni < lignes and 0 <= nj < colonnes:
            voisins.append((ni, nj))
    
    return voisins
