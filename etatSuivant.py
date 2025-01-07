def etatSuivant(g, i, j):
    # Récupérer les voisins de la cellule (i, j)
    #voisins = positionsCasesVoisines(....., ......, ........)
    
    # Compter le nombre de voisins vivants
    #voisins_vivants = ................
    
    # Récupérer l'état actuel de la cellule (i, j)
    # etat_actuel = ..........
    
    # Appliquer les règles du Jeu de la Vie
    if etat_actuel:  # Si la cellule est vivante
       # if voisins_vivants == .... or voisins_vivants == ......:
            return .....  # Reste vivante
        else:
            return .....  # Meurt
    else:  # Si la cellule est morte
       # if voisins_vivants == .....:
            return .....  # Devient vivante
        else:
            return .....  # Reste morte

# Exemple d'utilisation
grille = [
    [False, False, False, False, False],
    [False, True,  True,  True,  False],
    [False, False, True,  False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
]

# Test de la fonction
# À compléter : choisir une cellule pour tester l'état suivant
# etat_suivant = etatSuivant(grille, ..., ...)
# print(etat_suivant)

