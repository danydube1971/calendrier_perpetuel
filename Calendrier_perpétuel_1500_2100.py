"""Le script permet à l'utilisateur d'entrer une année, un mois et un jour de début pour afficher le calendrier mensuel correspondant.

La première partie du script vérifie que l'année, le mois et le jour de début sont valides en demandant à l'utilisateur d'entrer des valeurs numériques dans des plages spécifiées.

La deuxième partie utilise le module calendar pour créer un objet TextCalendar avec le jour de début spécifié, puis utilise la méthode formatmonth pour afficher le calendrier mensuel de l'année et du mois spécifiés. Le script a été modifié pour permettre à l'utilisateur de choisir de commencer le calendrier par dimanche ou par lundi.

Le script a également été modifié pour afficher le calendrier en français, en utilisant la locale française configurée avec l'encodage UTF-8.

En résumé, ce script permet à l'utilisateur de visualiser un calendrier mensuel pour une année et un mois donnés, avec un jour de début personnalisable et dans la langue de son choix (dans la limite des locales installées sur le système)."""

import calendar
import locale

def main():
    # Vérification de l'année
    while True:
        try:
            annee = int(input("Entrez une année entre 1500 et 2100: "))
            if 1500 <= annee <= 2100:
                break
            else:
                print("Veuillez entrer une année valide entre 1500 et 2100.")
        except ValueError:
            print("Veuillez entrer une année valide.")

    # Vérification du mois
    while True:
        try:
            mois = int(input("Entrez un mois entre 1 et 12: "))
            if 1 <= mois <= 12:
                break
            else:
                print("Veuillez entrer un mois valide entre 1 et 12.")
        except ValueError:
            print("Veuillez entrer un mois valide.")

    # Vérification du jour de début
    while True:
        try:
            debut = int(input("Entrez 0 pour commencer par dimanche ou 6 pour commencer par lundi: "))
            if debut == 0 or debut == 6:
                break
            else:
                print("Veuillez entrer 0 pour dimanche ou 6 pour lundi.")
        except ValueError:
            print("Veuillez entrer une valeur valide.")

    # Affichage du calendrier
    afficher_calendrier(annee, mois, debut)

def afficher_calendrier(annee, mois, debut):
    # Configurer la locale pour le français
    locale.setlocale(locale.LC_TIME, "fr_FR.utf8")

    # Inverser les valeurs de début pour commencer par dimanche
    if debut == 0:
        debut = 6
    else:
        debut = 0

    calendrier = calendar.TextCalendar(debut)
    calendrier_mensuel = calendrier.formatmonth(annee, mois)
    print("\n", calendrier_mensuel)

if __name__ == "__main__":
    main()

