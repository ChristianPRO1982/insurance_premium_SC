import common
import streamlit as st
from random import randint
from prediction import predict

title = "Estimateur"
st.set_page_config(page_title=title + " - " + common.title, page_icon=":skull:", layout="wide")
st.title(title)
common.sidebar()

if common.train_done:
    age = st.sidebar.slider("Age", 15, 120, 25)
    height = st.sidebar.slider("Taille (en cm)", 140, 250, 170)
    weight = st.sidebar.slider("Poids (en kg)", 30, 250, 70)
    sex = st.sidebar.radio("Sexe", ["Homme", "Femme", "Hasard"])
    smoker = st.sidebar.checkbox("Fumeur")

    # calcul de l'IMC
    bmi = round(weight / ((height / 100) ** 2), 2)

    # Afficher les données mises à jour
    st.write("Age :", age)
    st.write("IMC :", bmi)
    if sex == "Hasard":
        sex = "Femme"
        if randint(0, 1) == 0:
            sex = "Homme"
    st.write("Sexe :", sex)
    st.write("Fumeur :", smoker)
    st.write("___")
    st.write("# Prime d'assurance estimée à :", randint(15000, 88000))

st.title('Faites une simulation sans attendre!')

#affiche logo
#img = Image.open("logo.png")
#st.image(img, width=300)

#affiche bouton choix genre
gender = st.radio("Vous êtes un/une: ", ('Homme','Femme'))

# age
age = st.number_input("Sélectionnez votre âge", 0, 100)

#bmi
bmi = st.number_input("Sélectionnez votre IMC", 16, 55)

#case à cocher smoker
smoker = st.checkbox("Fumeur")

#bouton evaluation
st.button("Calculer ma prime")




