# Fichier....... : app_pi.py
# Rôle ......... : Afficher dans une application Streamlit :
#                  - la présence d'une date de naissance dans le million de décimales de Pi
#                  - le calcul des sommes des 20 premières et des 12² premières décimales de Pi
#                  - l'intégration d'une vidéo expliquant que la somme des entiers naturels est égale à -1/12
# Auteur ........: Camillia ALAMI CHENTOUFI
# Version .......: V1.0 du 20/05/2025 
# Licence .......: Outils Informatiques Collaboratifs – Chapitre 4.3

import streamlit as st
from datetime import datetime


# Lire le fichier et nettoyer le contenu
with open("pi_1_million.txt", "r") as f:
    pi_decimals = f.read().replace("\n", "").replace(" ", "").replace(":", "")


def check_birthday_in_pi(birthday):
    # Vérifie si la date est présente dans les décimales de Pi
    if birthday in pi_decimals:
        return f"La date {birthday} est présente dans les décimales de Pi !"
    else:
        return f"La date {birthday} n'est pas présente dans les décimales de Pi."

# Fonction pour calculer le jour de la semaine
def get_weekday(birthday):  
    try:
        # Vérifie la longueur de la chaîne pour déterminer le format de la date
        if len(birthday) == 6:
            # Format court (jjmmaa) : utilise %y pour représenter l'année sur 2 chiffres.
            # D'après la documentation mise dans mes sources :
            # %y : Année sans siècle (de 00 à 99), interprétée comme 19xx ou 20xx selon le contexte.
            # %Y : Année avec siècle (ex : 1999 ou 2025), représentée sur 4 chiffres.
            date_object = datetime.strptime(birthday, "%d%m%y")
        elif len(birthday) == 8:
            # Format long (jjmmAAAA), utilise %Y pour l'année sur 4 chiffres
            date_object = datetime.strptime(birthday, "%d%m%Y")
        else:
            # Si la longueur n'est ni 6 ni 8, retourne un message d'erreur
            return "Format invalide"
        # Utilise strftime() pour formater la date en jour de la semaine complet (ex : "Monday")
        return date_object.strftime("%A")
    except ValueError:
        # Cette exception est levée si la chaîne ne peut pas être convertie en date valide,
        # par exemple si la date est "310299" (29 février sur une année non bissextile)
        return "Date invalide"



# Interface Streamlit
st.title("Recherche de Date de Naissance dans Pi")
st.write("Entrez votre date de naissance au format jjmmaa.")

# Récupérer l'entrée utilisateur
user_birthday = st.text_input("Votre date de naissance (ex : 010199 ou 01012000)")

# Vérifier si la date est présente
if user_birthday:

    # Nettoyage des caractères spéciaux
    user_birthday = user_birthday.replace("/", "").replace("-", "")

    # Vérification dans Pi
    result = check_birthday_in_pi(user_birthday)
    st.success(result)
    
# Calcul du jour de la semaine
    weekday = get_weekday(user_birthday)
    st.info(f"Jour de la semaine : {weekday}")

# Calculer la somme des 20 premières décimales
sum_20 = sum(int(d) for d in pi_decimals[:20])

# Calculer la somme des 144 premières décimales (12^2)
sum_144 = sum(int(d) for d in pi_decimals[:12**2])


# Ajout à l'interface Streamlit
st.title("Calcul des sommes des premières décimales de Pi")
st.write(f"Somme des 20 premières décimales : {sum_20}")
st.write(f"Somme des 144 premières décimales : {sum_144}")

# Insertion d'une vidéo prise en ligne
st.header("Quelle est la somme de tous les nombres entiers naturels ?")
st.write("La vidéo suivante présente un résultat surprenant sur la somme des entiers naturels :")
st.video("https://www.youtube.com/watch?v=GnZQOb9YNV4")