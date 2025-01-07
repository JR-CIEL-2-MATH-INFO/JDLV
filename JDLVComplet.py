import time

import tkinter as tk

def afficherGrille(grille):
    """
    Affiche une grille de booléens dans une fenêtre Tkinter.
    Les cases avec True sont noires, et les autres sont blanches.
    """
    # Dimensions de la grille
    nombreLignes = len(grille)
    nombreColonnes = len(grille[0])
    
    # Taille des cases
    taille_case = 30  # Chaque case sera un carré de 30x30 pixels

    # Création de la fenêtre Tkinter
    fenetre = tk.Tk()
    fenetre.title("Grille de booléens")
    
    # Dimensions du canvas
    canvas = tk.Canvas(
        fenetre, 
        width=nombreColonnes * taille_case, 
        height=nombreLignes * taille_case
    )
    canvas.pack()

    # Dessin de la grille
    for i in range(nombreLignes):
        for j in range(nombreColonnes):
            couleur = "black" if grille[i][j] else "white"
            x1 = j * taille_case
            y1 = i * taille_case
            x2 = x1 + taille_case
            y2 = y1 + taille_case
            canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="gray")

    # Lancer la boucle principale Tkinter
    fenetre.mainloop()

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

def jeuDeLaVieAnimation(g, n):
    for step in range(n):
        print(f"État à l'étape {step + 1}:")
        afficherGrille(g)
        jeuDeLaVie(g)  # Mettre à jour la grille pour la prochaine étape
        time.sleep(1)  # Pause d'1 seconde pour mieux visualiser l'animation

# Exemple d'utilisation
grille = [
    [False, False, False, False, False],
    [False, True,  True,  True,  False],
    [False, False, True,  False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
]

# Afficher les 5 premiers états successifs
jeuDeLaVieAnimation(grille, 5)

