import common
import streamlit as st
from datetime import datetime, timedelta
from model import predict
import pandas as pd

title = "Faites une simulation sans attendre !"
st.set_page_config(page_title=title + " - " + common.title, page_icon="favicon.ico", layout="wide")
st.title(title)
common.sidebar(logo=False)

age = st.sidebar.slider("Age", 15, 120, 25)
height = st.sidebar.slider("Taille (en cm)", 140, 250, 170)
weight = st.sidebar.slider("Poids (en kg)", 30, 250, 70)
sex = st.sidebar.radio("Sexe", ["male", "female"])
smoker = st.sidebar.checkbox("Fumeur")
children = st.sidebar.slider("Nombre d'enfants", 0, 10, 0)
region = st.sidebar.selectbox('Sélectionnez votre région:', ('northeast', 'southeast', 'southwest', 'northwest'))

# calcul de l'IMC
bmi = round(weight / ((height / 100) ** 2), 2)

#convertir var categorielles en float
if sex == 'male': val_sex = 0
else: val_sex = 1
if smoker:
    val_smoker = 1
    val_smoker_txt = 'yes'
else:
    val_smoker = 0
    val_smoker_txt = 'no'
smoker_bmi = val_smoker * bmi
smoker_age = val_smoker * age
smoker_children = val_smoker * children
if bmi < 18.5:
    bmi_category = "Insuffisance pondérale"
elif bmi < 25:
    bmi_category = "Poids normal"
elif bmi < 30:
    bmi_category = "Surpoids"
elif bmi < 35:
    bmi_category = "Obésité modérée"
elif bmi < 40:
    bmi_category = "Obésité sévère"
else:
    bmi_category = "Obésité morbide"
if smoker:
    if bmi >= 30:
        charges_group = 3
    else:
        charges_group = 2
else:
    charges_group = 1

# Afficher les données mises à jour
col1, col2, col3 = st.columns(3)
txt_age = "Age : " + str(age)
col1.write(txt_age)
txt_sex = "Sexe : " + str(sex)
col1.write(txt_sex)
txt_children = "Nombre d'enfant : " + str(children)
col2.write(txt_children)
txt_region = "Région : " + str(region)
col2.write(txt_region)
txt_bmi = "IMC : " + str(bmi) + " >>> " + bmi_category
col3.write(txt_bmi)
txt_smoker = "Fumeur : " + str(smoker)
col3.write(txt_smoker)

st.write("___")

# data = [[age,val_sex,bmi,children,val_smoker,region, smoker_bmi, smoker_age, smoker_children]]# charges_group
data = [[age,sex,bmi,children,val_smoker_txt,region]]# charges_group
# columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'smoker_bmi', 'smoker_age', 'smoker_children']
columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
df = pd.DataFrame(data, columns=columns)

result = round(predict(df)[0], 2)
txt_result = "Estimation de la prime d'assurance : $" + str(result)
st.success(txt_result)
save_to_create = st.button("enregistrer ces données")

if save_to_create:
    st.session_state['age'] = age
    st.session_state['height'] = height
    st.session_state['weight'] = weight
    st.session_state['sex'] = val_sex
    st.session_state['smoker'] = smoker
    st.session_state['children'] = children
    st.session_state['region'] = region
    st.session_state['predict'] = result
    st.success("Les données sont sauvegardées")