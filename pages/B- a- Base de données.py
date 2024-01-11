import common
from pathlib import Path
import pandas as pd
import streamlit as st

title = "Base de données"
st.set_page_config(page_title=title + " - " + common.title, page_icon="favicon.ico", layout="wide")
st.title(title)
common.sidebar()

col1, col2 = st.columns(2)

# @st.cache_data
def load_data(csv_file):
   bikes_data_path = Path() / csv_file
   data = pd.read_csv(bikes_data_path)
   return data

df_base = load_data('data_cleaned_cheated.csv')
df_customer = load_data('data_custumer.csv')

col1.write("## Données récoltées")
col1.write(df_base)

col2.write('## Données clients')
col2.write(df_customer)

delete2 = False
delete1 = st.sidebar.button("Supprimer le dernier clients")
if delete1:
   common.supprimer_derniere_ligne('data_custumer.csv')
   st.rerun()
