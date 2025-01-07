def jeuDeLaVieAnimation(g, n):
    for step in range(n):
        print(f"État à l'étape {step + 1}:")
        afficherGrille(g)
        jeuDeLaVie(g)  # Mettre à jour la grille pour la prochaine étape
        time.sleep(1)  # Pause d'1 seconde pour mieux visualiser l'animation
