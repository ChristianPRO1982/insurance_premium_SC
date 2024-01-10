import common
import streamlit as st
import numpy as np
from random import randint
from  model import predict

#title = "Estimateur"
st.title('Faites une simulation sans attendre!')

#st.set_page_config(page_title=title + " - " + common.title, page_icon=":skull:", layout="wide")
#st.title(title)
common.sidebar()

if common.train_done:
    age = st.sidebar.slider("Age", 15, 120, 25)
    height = st.sidebar.slider("Taille (en cm)", 140, 250, 170)
    weight = st.sidebar.slider("Poids (en kg)", 30, 250, 70)
    sex = st.sidebar.radio("Sexe", ["Homme", "Femme"])
    smoker = st.sidebar.checkbox("Fumeur")
    region = st.sidebar.selectbox('Sélectionnez votre région:', ('northeast', 'southeast', 'southwest', 'northwest'))

    #convertir var categorielles en float
    if sex == 'Homme':
        val_sex = 0
    else:
        val_sex = 1

    if smoker == "Fumeur":
        val_smoker = 1
    else:
        val_smoker = 0
    val_region = float(val_smoker)
    

    # calcul de l'IMC
    bmi = round(weight / ((height / 100) ** 2), 2)

    # Afficher les données mises à jour
    st.write("Age :", age)
    st.write("IMC :", bmi)
    
    
    st.write("Sexe :", sex)
    st.write("Fumeur :", smoker)
    st.write("___")
    st.write("# Prime d'assurance estimée à :", randint(15000, 88000))


#affiche logo
#img = Image.open("logo.png")
#st.image(img, width=300)

# #affiche bouton choix genre
# gender = st.radio("Vous êtes un/une: ", ('Homme','Femme'))

# # age
# age = st.number_input("Sélectionnez votre âge", 0, 100)

# #bmi
# bmi = st.number_input("Sélectionnez votre IMC", 16, 55)

# #case à cocher smoker
# smoker = st.checkbox("Fumeur")

# #bouton evaluation
# st.button("Calculer ma prime")




