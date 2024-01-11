import common
from pathlib import Path
import pandas as pd
import streamlit as st

title = "Base de données"
st.set_page_config(page_title=title + " - " + common.title, page_icon=":skull:", layout="wide")
st.title(title)
common.sidebar()

col1, col2 = st.columns(2)

@st.cache_data
def load_data():
   bikes_data_path = Path() / 'data_cleaned_cheated.csv'
   data = pd.read_csv(bikes_data_path)
   return data

df_base = load_data()
df_customer = load_data()

col1.write("## Données récoltées")
col1.write(df_base)

col2.write('## Données clients')
col2.write(df_customer)

# first_name	last_name	birthday	age	sex	height	weight	bmi	children	smoker	region	charges
