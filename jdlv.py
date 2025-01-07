import tkinter as tk
grille = [
    [False, False, False, False, False, False, False],
    [False, False, False, False,  False, False, False],
    [False, True,  True,  True,  True,  True,  False],
    [False, False, False, True,  False, False, False],
    [False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False],
]

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

# Appel de la fonction pour afficher la grille
afficherGrille(grille)
