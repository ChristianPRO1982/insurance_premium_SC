import common
import streamlit as st
from random import randint
from datetime import datetime, timedelta
# from prediction import predict

date_minimale = datetime.today() - timedelta(days=365*100)

title = "Créer un(une) assuré(e)"
st.set_page_config(page_title=title + " - " + common.title, page_icon="favicon.ico", layout="wide")
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
region = col2.radio("Région d'habitation", ["Northeast", "Southeast", "Northwest", "Southwest"])

# calcul de l'IMC
bmi = round(weight / ((height / 100) ** 2), 2)

col3.write("## Santé")
col3.write(f"IMC : {bmi}")
smoker = col3.checkbox("Fumeur")

with st.sidebar.form(key='pre_confirm'):
    charges = st.number_input('Charges')
    discount = st.checkbox('remise vendeur ($-100)')
    submit = st.form_submit_button("Enregistrer le(la) nouvel(le) assuré(e)")
    # good = st.checkbox("Valider ces informations")

if submit:
    csv_file = 'data_custumer.csv'
    date_created = datetime.now()
    new_row = f'{first_name},{last_name},{birthday},{age},{sex},{height},{weight},{bmi},{children},{smoker},{region},{charges},{discount},{date_created}'
    with open(csv_file, 'a') as fichier:
        fichier.write(new_row + '\n')

    st.success("Les informations ont bien été enregistrées")
    
    