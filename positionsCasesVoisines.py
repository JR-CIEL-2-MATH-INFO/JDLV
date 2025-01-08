def positionsCasesVoisines(g, i, j):
    voisins = []
    #lignes = .........
    #colonnes = .......

    # Liste des directions possibles : haut, bas, gauche, droite, diagonales
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for di, dj in directions:
        #ni = .......
        #nj = .......
        # Vérifier si la nouvelle position est dans les limites de la grille
       # if 0 <= ni < lignes ..... 0 <= nj < colonnes:
            voisins.append((ni, nj))
    
    return voisins

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
print("Voisins :", voisins)

