from insurance_premium_SC.common import common
import streamlit as st
import numpy as np
from random import randint
from  model import predict
import joblib

#charge le modele 
modele_file = 'modele_insur.sav'
model = joblib.load(modele_file)

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

    features = [age, bmi, val_sex, val_smoker, val_region]

    predicted_charges = model.predict([features])

    # Afficher les données mises à jour
    st.write("Age :", age)
    st.write("IMC :", bmi)
    st.write("Sexe :", sex)
    st.write("Fumeur :", smoker)
    st.write("___")
    st.write("# Prime d'assurance estimée à :", predicted_charges[0])







