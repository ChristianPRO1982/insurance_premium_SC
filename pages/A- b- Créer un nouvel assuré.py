import common
import streamlit as st
from random import randint
from datetime import datetime, timedelta
# from prediction import predict

date_minimale = datetime.today() - timedelta(days=365*100)


title = "Créer un(une) assuré(e)"
st.set_page_config(page_title=title + " - " + common.title, page_icon=":skull:", layout="wide")
st.title(title)
common.sidebar()

col1, col2, col3 = st.columns(3)

col1.write("## Informations civils")
first_name = col1.text_input("Prénom")
last_name = col1.text_input("Nom")
sex = col1.radio("Sexe", ["Homme", "Femme"])
birthday = col1.date_input("Entrez votre date de naissance", min_value=date_minimale)
children = col1.slider("Nombre d'enfant", 0, 10, 0)

# calcul de l'age
today = datetime.today()
age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

col2.write("## Compléments")
height = col2.slider("Taille (en cm)", 140, 250, 170)
weight = col2.slider("Poids (en kg)", 30, 250, 70)
aaa = col2.slider("Combien de film au cinéma êtes-vous aller voir cette anée ?", 0, 50, 0)
region = col2.radio("Région d'habitation", ["Northeast", "Southeast", "Northwest", "Southwest"])

# calcul de l'IMC
bmi = round(weight / ((height / 100) ** 2), 2)

col3.write("## Santé")
col3.write(f"IMC : {bmi}")
smoker = col3.checkbox("Fumeur")
sex = col3.radio("La tête du client", ["C'est un pigeon", "Normale", "Il est cool, je lui fais une réduc."])

with st.sidebar.form(key='my_form'):
    submit = st.form_submit_button("Enregistrer le/la nouvel(le) assuré(e)")
    st.write(f"{first_name} {last_name}/{sex}/{age}/{children}/{region}/{bmi}/{smoker}")
    good = st.checkbox("Les valeurs sont OK")

if submit and good:
    good = False
    st.success("youpi !")


# Variable booléenne pour contrôler l'état du checkbox
etat_checkbox = False

# Affichage du checkbox initial
st.write("Valeur actuelle du checkbox :", etat_checkbox)

# Modifier la valeur du checkbox en fonction d'une condition
if st.button("Modifier le checkbox"):
    # Inversion de l'état actuel du checkbox
    etat_checkbox = not etat_checkbox

# Affichage du checkbox mis à jour
st.checkbox("Checkbox modifiable par le code", value=etat_checkbox)

