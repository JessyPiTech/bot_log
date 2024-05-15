import pyautogui
import time
import itertools

# Durée maximale de l'exécution en secondes
duree_maximale = 30

# Délai initial en secondes
delai_initial = 5

# Temps de début
temps_debut = time.time()

# Attendre le délai initial
time.sleep(delai_initial)

# Dictionnaire des coordonnées pour chaque chiffre
coordonnees_chiffres = {
    '0': (960, 750),
    '1': (850, 510),
    '2': (960, 510),
    '3': (1070, 510),
    '4': (850, 590),
    '5': (960, 590),
    '6': (1070, 590),
    '7': (850, 670),
    '8': (960, 670),
    '9': (1070, 670)
}

def cliquer_sur_chiffre(chiffre):
    if chiffre in coordonnees_chiffres:
        x, y = coordonnees_chiffres[chiffre]
        pyautogui.click(x=x, y=y)
    else:
        print("Coordonnées non définies pour le chiffre", chiffre)

def generer_combinaisons():
    chiffres = '0123456789'
    combinaisons = itertools.product(chiffres, repeat=4)
    return [''.join(combinaison) for combinaison in combinaisons]

def verifier_pixel_blanc(x, y, tolerance=35):
    # Récupérer la couleur du pixel
    couleur = pyautogui.pixel(x, y)
    print("Couleur du pixel à la position (", x, ",", y, "):", couleur)
    # Vérifier si les composantes R, G et B sont proches de 255 (blanc)
    blanc = all(abs(c - 255) < tolerance for c in couleur)
    # Retourner True si le pixel est blanc, sinon False
    return blanc

combinaisons_a_executer = generer_combinaisons()
derniere_combinaison = None

for combinaison in combinaisons_a_executer:
    if time.time() - temps_debut >= duree_maximale:
        break
    print("Combinaison en cours :", combinaison)
    for chiffre in combinaison:
        cliquer_sur_chiffre(chiffre)
    
    # Vérifier si un pixel spécifique est blanc ou gris
    if verifier_pixel_blanc(1120, 590):  # Modifier les coordonnées selon votre besoin
        derniere_combinaison = combinaison
       
    else:
        print("you win the code was ", combinaison,"ta trouver apres ", temps_debut"s ")
        break  # Arrêter l'exécution si le pixel n'est plus blanc

# Imprimer la dernière combinaison exécutée
if derniere_combinaison is not None:
    print("La dernière combinaison exécutée est :", derniere_combinaison)
else:
    print("Aucune combinaison n'a été exécutée.")

# Fin du script
print("Le script a été exécuté pendant", duree_maximale, "secondes.")