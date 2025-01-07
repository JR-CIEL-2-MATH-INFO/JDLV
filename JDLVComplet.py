




def jeuDeLaVieAnimation(g, n):
    for step in range(n):
        print(f"État à l'étape {step + 1}:")
        afficherGrille(g)
        jeuDeLaVie(g)  # Mettre à jour la grille pour la prochaine étape
        
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

