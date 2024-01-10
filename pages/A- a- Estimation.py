import common
import streamlit as st
from prediction import predict

title = "Estimateur"
st.set_page_config(page_title=title + " - " + common.title, page_icon=":skull:", layout="wide")
st.title(title)
common.sidebar()

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




