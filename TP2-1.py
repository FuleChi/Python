# Exercice 1. Demander à l'utilisateur de saisir l'heure, la minute et la seconde
# et de vérifier la validité des valeurs.

def valeur_saisie():
    heure = int(input("Entrez l'heure: "))
    while heure < 0 or heure > 24:
        heure = int(input("Entrez l'heure)

    minutes = int(input("Entrez les minutes : "))
    while minutes < 0 or minutes >= 60:
        minutes = int(input("Entrez minute)

    secondes = int(input("Entrez les secondes : "))
    while secondes < 0 or secondes >= 60:
        secondes = int(input("Entrez seconde)

    print(f"Voici l'heure saisie : {heure} h : {minutes} mn : {secondes} s")

def temps():
    valeur_saisie()

# Appel de la fonction
temps()


# #***************************EXERCICE 2***********************************************************
# #Calculer le salaire hebdomadaire en prenant en compte les heures supplémentaires

TAUX_SUPPL = 1.5
def calculer_salaire_hebdomadaire(heures_travaillees, salaire_horaire):
    if heures_travaillees > 40:
        heures_supplementaires = heures_travaillees - 40
        salaire = (40 * salaire_horaire) + (heures_supplementaires * salaire_horaire * TAUX_SUPPL)
    else:
        salaire = heures_travaillees * salaire_horaire
    return salaire

# Saisie de l'utilisateur
heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le taux horaire : "))

#Calcul et affichage du salaire hebdomadaire
salaire_hebdomadaire = calculer_salaire_hebdomadaire(heures_travaillees, salaire_horaire)
print(f"La paye est : {salaire_hebdomadaire:.1f} ")


#***************************EXERCICE 3***********************************************************
#Classer les notes en grades

def classer_note():
    bonnes_reponses = int(input("Entrez un nombre de bonnes réponses entre 0 et 50: "))

    while not (0 <= bonnes_reponses <= 50):
        bonnes_reponses = int(input("Entrez un nombre de bonnes réponses entre 0 et 50: "))

    if 0 <= bonnes_reponses <= 10:
        note = 'E'
    elif 11 <= bonnes_reponses <= 20:
        note = 'D'
    elif 21 <= bonnes_reponses <= 30:
        note = 'C'
    elif 31 <= bonnes_reponses <= 40:
        note = 'B'
    elif 41 <= bonnes_reponses <= 50:
        note = 'A'

    print(f"La note est : {note}")

# Appel de la fonction
classer_note()



