import common
from pathlib import Path
import pandas as pd
import streamlit as st

title = "Analyse"
st.set_page_config(page_title=title + " - " + common.title, page_icon="favicon.ico", layout="wide")
st.title(title)
common.sidebar()

donnees = st.sidebar.checkbox('Afficher les données')
y = st.sidebar.selectbox("Statistiques", ["age", "sex", "bmi", "smoker"])

col1, col2, col3, col4 = st.columns(4)
children = col1.checkbox("Enfants ?", value=False)
children_min = col1.slider("minimum", 0, 10, 1)
children_max = col1.slider("maximum", 0, 10, 1)
smoker = col2.checkbox("fumeur", value=True)
no_smoker = col2.checkbox("non fumeur", value=True)
male = col2.checkbox("homme", value=True)
female = col2.checkbox("femme", value=True)
region = col2.selectbox("Région", ["ALL", "northwest", "southwest", "northeast", "southeast"])
bmi1 = col3.checkbox("IMC : maigreur (<20)", value=True)
bmi2 = col3.checkbox("IMC : normal (>=20 & <25)", value=True)
bmi3 = col3.checkbox("IMC : surpoids (>=25 & <30)", value=True)
bmi4 = col3.checkbox("IMC : obésité modérée (>=30 & <35)", value=True)
bmi5 = col3.checkbox("IMC : obésité sévère (>=35 & <40)", value=True)
bmi6 = col3.checkbox("IMC : obésité massive (>=40)", value=True)
age = col4.checkbox("Age", value=False)
age_cur_min = col4.slider("Age minimum", 0, 100, 25)
age_cur_max = col4.slider("Age maximum", 0, 100, 50)

df = pd.read_csv("data_cleaned.csv")

if children == True:
    df = df.query(f'{children_min} <= children <= {children_max}')
if smoker == False:
    df = df[df['smoker'] != 1]
if no_smoker == False:
    df = df[df['smoker'] != 0]
if male == False:
    df = df[df['sex'] != 0]
if female == False:
    df = df[df['sex'] != 1]
if region != 'ALL':
    df = df[df['region'] == region]
if bmi1 == False:
    df = df[df['bmi'] >= 20]
if bmi2 == False:
    df = pd.concat([df[df['bmi'] < 20], df[df['bmi'] >= 25]], axis=0)
if bmi3 == False:
    df = pd.concat([df[df['bmi'] < 25], df[df['bmi'] >= 30]], axis=0)
if bmi4 == False:
    df = pd.concat([df[df['bmi'] < 30], df[df['bmi'] >= 35]], axis=0)
if bmi5 == False:
    df = pd.concat([df[df['bmi'] < 35], df[df['bmi'] >= 40]], axis=0)
if bmi6 == False:
    df = df[df['bmi'] < 40]
if age:
    df = df.query(f'{age_cur_min} <= age <= {age_cur_max}')


df = df.sort_values(by='charges', ascending=False)
if donnees:
    st.dataframe(df)
df = df[[y, 'charges']]
st.scatter_chart(df.set_index('charges'))
