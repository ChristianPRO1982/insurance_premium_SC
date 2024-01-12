import common
import streamlit as st
from random import randint
from datetime import datetime, timedelta

date_minimale = datetime.today() - timedelta(days=365*100)

title = "Créer un(une) assuré(e)"
st.set_page_config(page_title=title + " - " + common.title, page_icon="favicon.ico", layout="wide")
st.title(title)
common.sidebar()

col1, col2, col3 = st.columns(3)

col1.write("## Informations civils")
first_name = col1.text_input("Prénom")
last_name = col1.text_input("Nom")
sex = col1.radio("Sexe", ["Homme", "Femme"], index=st.session_state['sex'])
birthday = datetime.now()
birthday = birthday - timedelta(days=365 * st.session_state['age'])
birthday = col1.date_input("Entrez votre date de naissance", min_value=date_minimale, value=birthday)
children = col1.slider("Nombre d'enfant", 0, 10, st.session_state['children'])

# calcul de l'age
today = datetime.today()
age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

# index de la région
if st.session_state['region'] == 'northeast': index = 0
if st.session_state['region'] == 'southeast': index = 1
if st.session_state['region'] == 'northwest': index = 2
if st.session_state['region'] == 'southwest': index = 3

col2.write("## Compléments")
height = col2.slider("Taille (en cm)", 140, 250, st.session_state['height'])
weight = col2.slider("Poids (en kg)", 30, 250, st.session_state['weight'])
region = col2.radio("Région d'habitation", ["Northeast", "Southeast", "Northwest", "Southwest"], index=index)

# calcul de l'IMC
bmi = round(weight / ((height / 100) ** 2), 2)

col3.write("## Santé")
col3.write(f"IMC : {bmi}")
smoker = col3.checkbox("Fumeur", st.session_state['smoker'])

with st.sidebar.form(key='pre_confirm'):
    discount_amount = 500
    discount = st.checkbox('remise vendeur ($-' + str(discount_amount) + ')')
    charges = st.number_input('Charges', value=st.session_state['predict']) - discount_amount * discount
    submit = st.form_submit_button("Enregistrer le(la) nouvel(le) assuré(e)")
    # good = st.checkbox("Valider ces informations")

if submit:
    csv_file = 'data_custumer.csv'
    date_created = datetime.now()
    new_row = f'{first_name},{last_name},{birthday},{age},{sex},{height},{weight},{bmi},{children},{smoker},{region},{charges},{discount},{date_created}'
    with open(csv_file, 'a') as fichier:
        fichier.write(new_row + '\n')

    st.success("Les informations ont bien été enregistrées")