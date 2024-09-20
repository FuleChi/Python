import queue
import time

# Liste des comptes avec utilisateurs et mots de passe
comptes = [
    ("User1", "Psw1"),
    ("User2", "Psw2"),
    ("User3", "Psw3")
]

def verifier_identifiants(utilisateur, mot_de_passe):
    """Vérifie si le nom d'utilisateur et le mot de passe sont corrects"""
    for compte in comptes:
        if compte[0] == utilisateur and compte[1] == mot_de_passe:
            return True
    return False

def charger_et_decharger_file(liste):
    """Charge une liste dans une file, puis la décharge avec un délai"""
    # Créer une file
    file = queue.Queue()

    # Charger la liste triée dans la file
    for element in sorted(liste):
        file.put(element)

    # Décharger la file avec un délai
    while not file.empty():
        print(f"Élément déchargé: {file.get()}")
        time.sleep(10)  # Attendre 1 seconde entre chaque élément

# Demander les identifiants tant qu'ils ne sont pas corrects
identifiants_valides = False
while not identifiants_valides:
    # Demander le nom d'utilisateur et le mot de passe
    utilisateur = input("Entrez votre nom d'utilisateur: ")
    mot_de_passe = input("Entrez votre mot de passe: ")

    # Vérification des identifiants
    if verifier_identifiants(utilisateur, mot_de_passe):
        print("Accès autorisé.")
        identifiants_valides = True

        # Créer une liste de 10 valeurs différentes
        liste_valeurs = [10, 20, 30, 5, 25, 15, 40, 35, 45, 50]

        # Appeler la fonction pour charger et décharger la file
        charger_et_decharger_file(liste_valeurs)
    else:
        print("Accès refusé. Nom d'utilisateur ou mot de passe incorrect. Veuillez réessayer.")


