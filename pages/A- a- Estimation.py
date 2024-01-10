import common
import streamlit as st
import numpy as np
from random import randint
from  model import predict

title = "Estimateur"
st.set_page_config(page_title=title + " - " + common.title, page_icon=":skull:", layout="wide")
st.title(title)
common.sidebar()

if common.train_done:
    age = st.sidebar.slider("Age", 15, 120, 25)
    height = st.sidebar.slider("Taille (en cm)", 140, 250, 170)
    weight = st.sidebar.slider("Poids (en kg)", 30, 250, 70)
    sex = st.sidebar.radio("Sexe", ["Homme", "Femme"])
    smoker = st.sidebar.checkbox("Fumeur")

    #convertir sex en float
    if sex == 'Homme':
        val_sex = 0
    else:
        val_sex = 1

    # calcul de l'IMC
    bmi = round(weight / ((height / 100) ** 2), 2)

    # Afficher les données mises à jour
    st.write("Age :", age)
    st.write("IMC :", bmi)
    
    
    st.write("Sexe :", sex)
    st.write("Fumeur :", smoker)
    st.write("___")
    st.write("# Prime d'assurance estimée à :", predict(np.array([age, val_sex, bmi, smoker])))



#st.title('Faites une simulation sans attendre!')

#affiche logo
#img = Image.open("logo.png")
#st.image(img, width=300)

#affiche bouton choix genre







